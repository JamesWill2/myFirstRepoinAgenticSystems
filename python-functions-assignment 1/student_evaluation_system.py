def greet_student(name):
    return "Hello, " + name


def analyze_scores(scores):
    total_subjects = len(scores)
    average_score = sum(scores) / total_subjects
    return total_subjects, average_score


def evaluate_result(average):
    if average >= 50:
        return "Pass"
    else:
        return "Fail"


def main():
    name = "Rahul"
    scores = [60, 45, 70, 55]

    greeting = greet_student(name)
    subjects, average = analyze_scores(scores)
    result = evaluate_result(average)

    print(greeting)
    print("Subjects:", subjects)
    print("Average score:", average)
    print("Result:", result)


main()