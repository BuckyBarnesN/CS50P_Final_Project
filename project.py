import csv
from collections import Counter
import re

# all the functions which print the charts are in the file charts.py
import charts

def main():

    # list of dictionaries
    # each line in a csv file is a dictionary
    workout_data = []
    try:
        with open ("data.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                workout_data.append(row)
    except IOError:
        print("Error: File does not appear to exist")

    # clean up the data
    cleaned_with_duplicates = cleanup_1(workout_data)

    #print(cleaned_with_duplicates)

    # extract the rep ranges worked with and display them in a bar graph
    # would have liked to use pie charts but > 5 values
    reps, frequency = popular_rep_ranges(cleaned_with_duplicates)
    charts.bar_popular_rep_ranges(reps, frequency)

    # extract the body part trained and display their freqency in a pie chart
    body_part, frequency = muscles_worked(cleaned_with_duplicates)
    charts.pie_muscles_worked(body_part, frequency)

    # remove duplicate entries
    cleaned_without_duplicates = cleanup_2(cleaned_with_duplicates)
    
    #with open("cleaned.csv", "a") as file:
    #    writer = csv.DictWriter(file, fieldnames=["Date", "Exercise", "Category", "Weight", "Reps"])
    #    for workout in cleaned_without_duplicates:
    #        writer.writerow({"Date": workout["Date"], "Exercise": workout["Exercise"], "Category": workout["Category"], "Weight": workout["Weight"], "Reps": workout["Reps"]})

    # Progression for each of the lifts Squats, Deadlifts, Bench Press, OHP
    back_squat = get_weight(cleaned_without_duplicates, "Barbell Squat")
    charts.line_progression(back_squat, "Back Squat")

    deadlift = get_weight(cleaned_without_duplicates, "Deadlift")
    charts.line_progression(deadlift, "Deadlift")

    bench_press = get_weight(cleaned_without_duplicates, "Flat Barbell Bench Press")
    charts.line_progression(bench_press, "Bench Press")

    ohp = get_weight(cleaned_without_duplicates, "Overhead Press")
    charts.line_progression(ohp, "Overhead Press")

    # ratio of ohp:bench:squat:deadlift
    charts.bar_lifts_ratio(max(ohp), max(bench_press), max(back_squat), max(deadlift))

    # progression of back vs front squats
    front_squat = get_weight(cleaned_without_duplicates, "Barbell Front Squat")
    charts.line_comp_front_back_squats(front_squat, back_squat)

    # what exercise do i do most frequently?
    exercise, frequency = get_exercises(cleaned_with_duplicates)
    charts.pie_exercises_performed(exercise, frequency)
    

def cleanup_1(data):
    """
    Cleanup the data.
    Distance, distance unit and time are empty fields.
    If comment == "snatch grip deadlift" then change the name to Snatch Grip Deadlifts

    :param data: workout data as csv
    :type data: list of dictionaries
    :return: Cleaned up data
    :rtype: list of dictionaries
    """
    
    for workout in data:
        del workout["Distance"], workout["Distance Unit"], workout["Time"]
        # if the comment says Snatch grip turn the name into "Snatch Grip Deadlift"
        if re.match(r"snatch ?grip", workout["Comment"], re.IGNORECASE):
            workout["Exercise"] = "Snatch-Grip Deadlift"
        # now the comment can also be omitted
        del workout["Comment"]
        # change deadlifts to lower body exericse
        if workout["Exercise"] == "Deadlift" or workout["Exercise"] == "Snatch-Grip Deadlift":
            workout["Category"] = "Legs and Back (Deadlift(variation))"
        # since all the weights are in kgs can omit Weight Unit as well
        del workout["Weight Unit"]
    
    return data

def cleanup_2(data):
    """
    Cleanup the data.
    Remove duplicate entries with multiple similar entries.

    :param data: semi cleaned data as csv
    :type data: list of dictionaries
    :return: Cleaned up data with no two duplicate entries
    :rtype: list of dictionaries
    """
    # using list comprehension to remove duplicate dictionary
    without_dupes = [i for n, i in enumerate(data)
                     if i not in data[:n]]

    return without_dupes


def popular_rep_ranges(data):
    """
    Gives an insight of the rep ranges worked with.
    returns lists of reps and corresponding frequency

    :param data: cleaned up data
    :type data: list of dicts
    :return: reps and the corresponding frequency
    :rtype: list of ints
    """

    # could have done other way with .update but somehow my input splitted. eg: Reps 15 became 1 and 5
    reps = [workout["Reps"] for workout in data]

    count = Counter(reps)

    # count.most_common() gives a list of tuples
    reps = [scheme[0] for scheme in count.most_common(len(count))]
    frequency = [scheme[1] for scheme in count.most_common(len(count))]

    #print(reps)
    #print(frequency)
    return reps, frequency

def muscles_worked(data):
    """
    Gives an insight on how often a muscle group was trained

    :param data: cleaned up data
    :type data: list of dicts
    :return: muscle group and corresponding training frequency
    :rtype: list of ints 
    """

    category = [workout["Category"] for workout in data]
    
    count = Counter(category)

    body_part = [scheme[0] for scheme in count.most_common(len(count))]
    frequency = [int(scheme[1]) for scheme in count.most_common(len(count))]
    
    return body_part, frequency

def get_weight(data, exercise):
    """
    Returns date and back squat weight

    :param data: cleaned up data without duplicates
    :type data: list of dicts
    :param exercise: which exercise to extract weight for
    :type exercise: str
    :return: weight of back squats
    :rtype: list of ints
    """
    weights = [workout["Weight"] for workout in data if workout["Exercise"] == exercise]

    # the weights are str 
    # convert the weights to int

    weights = [eval(weight) for weight in weights]

    return weights

def get_exercises(data):
    """
    Gives an insight on how often an exercise was performed

    :param data: cleaned up data
    :type data: list of dicts
    
    """
    exercise = [workout["Exercise"] for workout in data]
    
    count = Counter(exercise)

    exercise = [scheme[0] for scheme in count.most_common(5)]
    frequency = [int(scheme[1]) for scheme in count.most_common(5)]
    
    return exercise, frequency

if __name__ == "__main__":
    main()