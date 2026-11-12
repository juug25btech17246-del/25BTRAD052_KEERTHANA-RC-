# Mini Project (Unit 2): Student Grading Automation System
# Concepts used: functions, loops, conditionals, dictionaries, string formatting

SUBJECTS = ["Maths", "Physics", "Python"]


def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


def calculate_result(marks):
    total = sum(marks)
    average = total / len(marks)
    grade = calculate_grade(average)
    status = "Pass" if all(m >= 35 for m in marks) and grade != "F" else "Fail"
    return total, average, grade, status


def collect_students():
    students = {}
    n = int(input("Enter number of students: "))
    for i in range(n):
        print(f"\n--- Student {i + 1} ---")
        name = input("Enter student name: ").strip()
        marks = []
        for subject in SUBJECTS:
            mark = int(input(f"Enter marks in {subject} (out of 100): "))
            marks.append(mark)
        students[name] = marks
    return students


def display_report_card(students):
    print("\n" + "=" * 70)
    print(f"{'STUDENT GRADE REPORT':^70}")
    print("=" * 70)

    header = f"{'Name':<12}"
    for subject in SUBJECTS:
        header += f"{subject:>10}"

    header += f"{'Total':>8}{'Avg':>8}{'Grade':>8}{'Result':>10}"
    print(header)
    print("-" * 70)

    topper_name = None
    topper_avg = -1

    for name, marks in students.items():
        total, average, grade, status = calculate_result(marks)
        row = f"{name:<12}"

        for m in marks:
            row += f"{m:>10}"

        row += f"{total:>8}{average:>8.2f}{grade:>8}{status:>10}"
        print(row)

        if average > topper_avg:
            topper_avg = average
            topper_name = name

    print("=" * 70)
    print(f"Class Topper: {topper_name} (Average: {topper_avg:.2f})")
    print("=" * 70)


# ---- Program starts here ----
students = collect_students()

if students:
    display_report_card(students)
else:
    print("No student data entered.")