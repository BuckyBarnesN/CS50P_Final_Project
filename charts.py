from matplotlib import pyplot as plt

def bar_popular_rep_ranges(reps, frequency):
    """
    Bar chart of reps and corresponding frequency

    :param reps: rep schemes
    :param frequency: corresponding frequency
    :type reps, frequency: list of ints
    :return: None
    """
    
    plt.style.use("grayscale")

    plt.bar(reps, frequency)
    plt.title("Common rep scheme")
    plt.xlabel("Reps")
    plt.ylabel("Frequency")

    plt.grid()
    plt.tight_layout()

    plt.savefig("rep_schemes.png")
    plt.show()

def pie_muscles_worked(body_part, frequency):
    """
    Pie chart of body part worked and their frequency

    :param body_part: body_part worked
    :param frequency: corresponding frequency
    :type body_part: list of str
    :type frequency: list of ints
    :return: None
    """

    plt.style.use("bmh")

    plt.title("Bodyparts worked")
    plt.pie(frequency, labels=body_part, autopct="%1.1f%%",wedgeprops={"edgecolor": "black"})
    plt.tight_layout()
    plt.savefig("bodyparts_worked.png")
    plt.show()

def line_progression(weights, exercise):
    """
    Line chart of exercise progression

    :param weights: squats weight on different workouts
    :type weight: list of int
    :param exercise: exercise selection
    :type exercise: str
    :return: None
    """

    #print(weights)

    #print(plt.style.available)
    plt.style.use("ggplot")
    plt.plot(weights, marker = "o")

    plt.xlabel("Workouts")
    plt.ylabel("Weight (kg)")
    # this is to hide the workout dates
    plt.xticks(color = "w")
    plt.title(exercise + " progression")

    plt.savefig(f"{exercise}_progression.png")

    plt.tight_layout()
    plt.show()

def bar_lifts_ratio(ohp, bench, squat, deadlift):
    """
    Bar chart of the exercise max weight ratio

    :param ohp: max ohp weight
    :type ohp: int
    :param bench: max bench weight
    :type bench: int
    :param squat: max squat weight
    :type squat: int
    :param deadlift: max deadlift weight
    :type deadlift: int
    :return: None

    """

    plt.style.use("seaborn-v0_8-whitegrid")

    lifts = ["Overhead Press", "Bench Press", "Back Squat", "Deadlift"]
    corresponding_weights = [ohp, bench, squat, deadlift]

    plt.bar(lifts, corresponding_weights)
    plt.title("Ratio of OHP:Bench:Squat:Deadlift\n\n(Optimal 2:3:4:5)")
    
    plt.ylabel("Weight(kg)")

    plt.tight_layout()

    plt.savefig("Lifts_Ratio.png")

    plt.show()

def line_comp_front_back_squats(front, back):
    """
    line progression of front vs back squats

    :param front: weights in front squat
    :type front: list of ints
    :param back: weights in back squat
    :type back: list of ints
    :return: None

    """
    #print(plt.style.available)
    plt.style.use("classic")

    plt.plot(front, label="Front Squats", marker="o")
    plt.plot(back, label="Back Squat", marker="o")

    plt.xlabel("Workouts")
    plt.ylabel("Weight (kg)")
    plt.title("Progression of front vs back squats")
    plt.grid(True)

    plt.legend()

    plt.tight_layout()

    plt.savefig("front_vs_back_squat.png")
    plt.show()
    
def pie_exercises_performed(exercise, frequency):
    """
    Pie chart of top 5 exercises performed along with its frequency

    :param exercise: list of exercises
    :type exercises: list of str
    :param frequency: corresponding frequency of exercises performed
    :type frequency: list of int
    :return: None
    """

    plt.style.use("fivethirtyeight")

    plt.title("Most performed exercises")
    plt.pie(frequency, labels=exercise, autopct="%1.1f%%",wedgeprops={"edgecolor": "black"})
    plt.tight_layout()
    plt.savefig("top_exercises.png")
    plt.show()