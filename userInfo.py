import tkinter as tk
from tkinter import messagebox

# Predefined username and password
VALID_USERNAME = "admin"
VALID_PASSWORD = "password123"

# Function to check username and password
def check_credentials():
    entered_username = username_entry.get()
    entered_password = password_entry.get()
    
    if entered_username == VALID_USERNAME and entered_password == VALID_PASSWORD:
        messagebox.showinfo("Login Success", "Welcome!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create main window
app = tk.Tk()
app.title("Login Form")
app.geometry("300x200")

# Username label and entry
username_label = tk.Label(app, text="Username:")
username_label.pack(pady=5)

username_entry = tk.Entry(app, width=30)
username_entry.pack(pady=5)

# Password label and entry
password_label = tk.Label(app, text="Password:")
password_label.pack(pady=5)

password_entry = tk.Entry(app, show="*", width=30)  # 'show' hides the password input
password_entry.pack(pady=5)

# Login button
login_button = tk.Button(app, text="Login", command=check_credentials)
login_button.pack(pady=10)

# Run the application
app.mainloop()
