students = {}

n = int(input("Number of students: "))

for i in range(n):
    name = input("Name: ")
    students[name] = int(input("Marks: "))

for name, marks in students.items():
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 35:
        grade = "D"
    else:
        grade = "Fail"

    print(name, marks, grade)