import csv
from datetime import datetime

# Dictionary to store student information
students = {}

def add_student():
    roll_number = input("Enter roll number: ").upper()
    name = input("Enter student name: ").title()
    if roll_number in students:
        print("Student already exists.")
    else:
        students[roll_number] = {'name': name, 'attendance': {}}
        print("Student added successfully.")

def mark_attendance():
    roll_number = input("Enter roll number: ").upper()
    if roll_number not in students:
        print("Student not found.")
        return
    date = datetime.now().strftime("%Y-%m-%d")
    if date in students[roll_number]['attendance']:
        print("Attendance for today is already marked.")
    else:
        status = input("Enter status (present/absent): ").lower()
        if status in ['present', 'absent']:
            students[roll_number]['attendance'][date] = status
            print("Attendance marked successfully.")
        else:
            print("Invalid status. Please enter 'present' or 'absent'.")

def view_attendance_for_student():
    roll_number = input("Enter roll number: ").upper()
    if roll_number not in students:
        print("Student not found.")
        return
    student = students[roll_number]
    print(f"Attendance for {student['name']} (Roll Number: {roll_number}):")
    for date, status in student['attendance'].items():
        print(f"Date: {date}, Status: {status}")

def view_attendance_for_all():
    if not students:
        print("No students found.")
        return
    print("Attendance for all students:")
    for roll_number, student in students.items():
        print(f"\nStudent Name: {student['name']}, Roll Number: {roll_number}")
        for date, status in student['attendance'].items():
            print(f"Date: {date}, Status: {status}")

def save_data():
    with open('attendance_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Roll Number', 'Name', 'Date', 'Status'])
        for roll_number, student in students.items():
            for date, status in student['attendance'].items():
                writer.writerow([roll_number, student['name'], date, status])
    print("Data saved successfully.")

def load_data():
    try:
        with open('attendance_data.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                roll_number = row['Roll Number']
                if roll_number not in students:
                    students[roll_number] = {'name': row['Name'], 'attendance': {}}
                students[roll_number]['attendance'][row['Date']] = row['Status']
        print("Data loaded successfully.")
    except FileNotFoundError:
        print("No saved data found.")

def main():
    load_data()
    while True:
        print("\nStudent Attendance System")
        print("1. Add New Student")
        print("2. Mark Attendance")
        print("3. View Attendance for a Specific Student")
        print("4. View Attendance for All Students")
        print("5. Save Data to File")
        print("6. Load Data from File")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        if choice == '1':
            add_student()
        elif choice == '2':
            mark_attendance()
        elif choice == '3':
            view_attendance_for_student()
        elif choice == '4':
            view_attendance_for_all()
        elif choice == '5':
            save_data()
        elif choice == '6':
            load_data()
        elif choice == '7':
            save_data()  # Save data before exiting
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
