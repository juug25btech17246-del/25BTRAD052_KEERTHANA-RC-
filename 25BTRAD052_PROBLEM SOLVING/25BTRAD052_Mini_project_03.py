student_names = []
attendance = {}

def add_student():
    name = input("Enter student name: ").strip()
    if name == "":
        print("Name cannot be empty.")
    elif name in attendance:
        print("Student already exists.")
    else:
        student_names.append(name)
        attendance[name] = []
        print("Student added successfully.")

def mark_attendance():
    name = input("Enter student name: ").strip()
    if name not in attendance:
        print("Student not found. Add the student first.")
        return

    status = input("Enter attendance (P/A): ").strip().upper()
    if status == "P" or status == "A":
        attendance[name].append(status)
        print("Attendance recorded successfully.")
    else:
        print("Invalid status. Enter P or A.")

def display_records():
    if not student_names:
        print("No student records available.")
        return

    print("\nName         Present Absent Records")
    print("----------------------------------------")
    for name in student_names:
        records = attendance[name]
        present = records.count("P")
        absent = records.count("A")
        print(f"{name:<10} {present:<8} {absent:<7} {records}")

def show_percentages():
    if not student_names:
        print("No student records available.")
        return

    print("\nAttendance Percentage")
    for name in student_names:
        records = attendance[name]
        total = len(records)
        if total == 0:
            percentage = 0
        else:
            percentage = (records.count("P") / total) * 100
        print(f"{name}: {percentage:.2f}%")

def below_threshold():
    try:
        threshold = float(input("Enter attendance threshold (%): "))
        if threshold < 0 or threshold > 100:
            print("Enter a threshold from 0 to 100.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    found = False
    for name in student_names:
        records = attendance[name]
        total = len(records)
        percentage = (records.count("P") / total * 100) if total > 0 else 0
        if percentage < threshold:
            print(f"{name}: {percentage:.2f}%")
            found = True

    if not found:
        print("No students are below the threshold.")

while True:
    print("\n--- ATTENDANCE TRACKER ---")
    print("1. Add student")
    print("2. Mark attendance")
    print("3. Display attendance records")
    print("4. Show attendance percentages")
    print("5. Identify students below threshold")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_student()
    elif choice == "2":
        mark_attendance()
    elif choice == "3":
        display_records()
    elif choice == "4":
        show_percentages()
    elif choice == "5":
        below_threshold()
    elif choice == "6":
        print("Exiting Attendance Tracker. Thank you!")
        break
    else:
        print("Invalid choice. Please try again.")