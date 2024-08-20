import datetime

# Initialize the student attendance dictionary
attendance = {}

def mark_attendance(student_name):
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    if date not in attendance:
        attendance[date] = {}
    attendance[date][student_name] = "Present"
    print(f"Attendance marked for {student_name} on {date}.")

def view_attendance():
    for date, students in attendance.items():
        print(f"\nDate: {date}")
        for student, status in students.items():
            print(f"Student: {student}, Status: {status}")

def main():
    while True:
        print("\nStudent Attendance System")
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            student_name = input("Enter the student's name: ").strip()
            mark_attendance(student_name)
        elif choice == '2':
            view_attendance()
        elif choice == '3':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
