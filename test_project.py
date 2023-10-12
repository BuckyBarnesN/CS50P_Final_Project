import project
import csv

workout_data = []
try:
    with open ("sample_data.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
                workout_data.append(row)
except IOError:
    print("Error: File does not appear to exist")

cleaned_with_duplicates = project.cleanup_1(workout_data)

cleaned_without_duplicates = project.cleanup_2(cleaned_with_duplicates)

def test_popular_rep_ranges():
    reps, frequency = project.popular_rep_ranges(cleaned_with_duplicates)
    reps = [int(rep) for rep in reps]
    frequency = [int(freq) for freq in frequency]

    # comes in descending order
    assert frequency == [10, 5, 4, 3, 2, 1]
    assert reps == [5, 2, 3, 10, 1, 4]

def test_muscles_worked():
     body_part, frequency = project.muscles_worked(cleaned_with_duplicates)

     assert body_part == ["Legs", "Chest", "Legs and Back (Deadlift(variation))", "Shoulders"]
     assert frequency == [13, 5, 4 ,3]

def test_get_weight():
    deadlift = project.get_weight(cleaned_without_duplicates, "Deadlift")

    assert deadlift == [92.5, 95.0]

def test_get_exercises():
     exercise, frequency = project.get_exercises(cleaned_with_duplicates)

     assert exercise == ["Barbell Front Squat", "Flat Barbell Bench Press", "Barbell Squat", "Deadlift", "Overhead Press"]
     assert frequency == [9, 5, 4, 4, 3]