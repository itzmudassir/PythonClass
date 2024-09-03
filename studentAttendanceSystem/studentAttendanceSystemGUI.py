import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv
from datetime import datetime
import os

try:
    import ttkbootstrap as tb
except ImportError:
    print("ttkbootstrap is not installed. Run 'pip install ttkbootstrap' to install it.")
    exit()

# Define the folder path for storing CSV files
folder_path = os.path.join(os.path.dirname(__file__), 'csvFiles')

# Ensure the folder exists
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# File paths
students_file = os.path.join(folder_path, 'students.csv')
attendance_file = os.path.join(folder_path, 'attendance.csv')

# Initialize main application window
app = tb.Window(themename="superhero")
app.title("Student Attendance System")
app.geometry("800x650")
app.resizable(False, False)

# Global dictionaries to store data
students = {}
attendance = {}

# Function to load students data
def load_students():
    if os.path.exists(students_file):
        with open(students_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                roll_number = row['Roll Number']
                name = row['Name']
                students[roll_number] = name
        print("Students data loaded successfully.")
    else:
        print("students.csv file not found. Starting with empty student list.")

# Function to load attendance data
def load_attendance():
    if os.path.exists(attendance_file):
        with open(attendance_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                roll_number = row['Roll Number']
                datetime_marked = row['Date & Time']
                status = row['Status']
                if roll_number in attendance:
                    attendance[roll_number][datetime_marked] = status
                else:
                    attendance[roll_number] = {datetime_marked: status}
        print("Attendance data loaded successfully.")
    else:
        print("attendance.csv file not found. Starting with empty attendance records.")

# Function to save students data
def save_students():
    with open(students_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Roll Number', 'Name'])
        for roll_number, name in students.items():
            writer.writerow([roll_number, name])
    print("Students data saved successfully.")

# Function to save attendance data
def save_attendance():
    with open(attendance_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Roll Number', 'Date & Time', 'Status'])
        for roll_number, records in attendance.items():
            for datetime_marked, status in records.items():
                writer.writerow([roll_number, datetime_marked, status])
    print("Attendance data saved successfully.")

# Function to add a new student
def add_student():
    def save_new_student():
        roll_number = roll_entry.get().upper()
        name = name_entry.get().title()
        if roll_number in students:
            messagebox.showerror("Error", "Student already exists.")
        else:
            students[roll_number] = name
            save_students()
            messagebox.showinfo("Success", "Student added successfully.")
            add_window.destroy()

    add_window = tb.Toplevel(app)
    add_window.title("Add New Student")
    add_window.geometry("500x250")
    add_window.resizable(False, False)

    roll_label = ttk.Label(add_window, text="Roll Number:")
    roll_label.pack(pady=5)
    roll_entry = ttk.Entry(add_window)
    roll_entry.pack(pady=5)

    name_label = ttk.Label(add_window, text="Student Name:")
    name_label.pack(pady=5)
    name_entry = ttk.Entry(add_window)
    name_entry.pack(pady=5)

    save_button = ttk.Button(add_window, text="Save", command=save_new_student)
    save_button.pack(pady=10)

# Function to mark attendance
def mark_attendance():
    def save_attendance_status():
        roll_number = roll_entry.get().upper()
        status = status_combobox.get().lower()
        if roll_number not in students:
            messagebox.showerror("Error", "Student not found.")
        else:
            datetime_marked = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if roll_number in attendance:
                attendance[roll_number][datetime_marked] = status
            else:
                attendance[roll_number] = {datetime_marked: status}
            save_attendance()
            messagebox.showinfo("Success", "Attendance marked successfully.")
            attendance_window.destroy()

    attendance_window = tb.Toplevel(app)
    attendance_window.title("Mark Attendance")
    attendance_window.geometry("500x250")
    attendance_window.resizable(False, False)

    roll_label = ttk.Label(attendance_window, text="Roll Number:")
    roll_label.pack(pady=5)
    roll_entry = ttk.Entry(attendance_window)
    roll_entry.pack(pady=5)

    status_label = ttk.Label(attendance_window, text="Status (Present/Absent):")
    status_label.pack(pady=5)
    status_combobox = ttk.Combobox(attendance_window, values=["Present", "Absent"], state="readonly")
    status_combobox.pack(pady=5)

    save_button = ttk.Button(attendance_window, text="Save", command=save_attendance_status)
    save_button.pack(pady=10)

# Function to view specific student attendance
def view_student_attendance():
    def show_attendance():
        roll_number = roll_entry.get().upper()
        if roll_number not in students:
            messagebox.showerror("Error", "Student not found.")
        else:
            attendance_window = tb.Toplevel(app)
            attendance_window.title(f"Attendance for {students[roll_number]}")
            attendance_window.geometry("500x250")
            attendance_window.resizable(False, False)

            for datetime_marked, status in attendance.get(roll_number, {}).items():
                record_label = ttk.Label(attendance_window, text=f"{datetime_marked}: {status.title()}")
                record_label.pack(pady=2)

    view_window = tb.Toplevel(app)
    view_window.title("View Student Attendance")
    view_window.geometry("500x250")
    view_window.resizable(False, False)

    roll_label = ttk.Label(view_window, text="Roll Number:")
    roll_label.pack(pady=5)
    roll_entry = ttk.Entry(view_window)
    roll_entry.pack(pady=5)

    view_button = ttk.Button(view_window, text="View", command=show_attendance)
    view_button.pack(pady=10)

# Function to view attendance for all students
def view_all_attendance():
    view_all_window = tb.Toplevel(app)
    view_all_window.title("View All Attendance")
    view_all_window.geometry("500x250")
    view_all_window.resizable(False, False)

    for roll_number, records in attendance.items():
        student_label = ttk.Label(view_all_window, text=f"\nStudent: {students[roll_number]} (Roll: {roll_number})")
        student_label.pack(pady=5)
        for datetime_marked, status in records.items():
            record_label = ttk.Label(view_all_window, text=f"{datetime_marked}: {status.title()}")
            record_label.pack(pady=2)

# Load data at startup
load_students()
load_attendance()

# Main Frame
main_frame = ttk.Frame(app, padding=20)
main_frame.pack(expand=True, fill='both')

# Title Label
title_label = ttk.Label(main_frame, text="Student Attendance System", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

# Buttons Frame
buttons_frame = ttk.Frame(main_frame)
buttons_frame.pack(pady=20)

# Buttons
add_student_btn = ttk.Button(buttons_frame, text="Add New Student", width=25, command=add_student)
mark_attendance_btn = ttk.Button(buttons_frame, text="Mark Attendance", width=25, command=mark_attendance)
view_student_attendance_btn = ttk.Button(buttons_frame, text="View Specific Student Attendance", width=25, command=view_student_attendance)
view_all_attendance_btn = ttk.Button(buttons_frame, text="View All Attendance", width=25, command=view_all_attendance)
exit_btn = ttk.Button(buttons_frame, text="Exit", width=25, command=app.quit)

# Placing buttons
add_student_btn.pack(pady=5)
mark_attendance_btn.pack(pady=5)
view_student_attendance_btn.pack(pady=5)
view_all_attendance_btn.pack(pady=5)
exit_btn.pack(pady=5)

# Run the application
app.mainloop()
