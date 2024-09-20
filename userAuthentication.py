import tkinter as tk
from tkinter import messagebox

app = tk.Tk()
app.title("User Authentication")
app.geometry("300x200")
app.configure(bg='lightblue')

VALID_USERNAME = "admin"
VALID_PASSWORD = "admin"

def check_credentiials():
    enteredUsername= userNameEntry.get().strip()
    enteredPassword = passwordEntry.get().strip()
    
    if enteredUsername == VALID_USERNAME and enteredPassword == VALID_PASSWORD:
        messagebox.showinfo("Login Successful", "Welcome")
        
    else:
        messagebox.showerror("Login Failed", "Invalid username and password")
        

# Username Label and Entry
userNameLabel = tk.Label(app, text='Username', fg="#00fefb")
userNameLabel.grid(row=0, column=0)

userNameEntry = tk.Entry(app)
userNameEntry.grid(row=0, column=1)

# Password Label and Entry
passwordLabel = tk.Label(app, text="Password")
passwordLabel.grid(row=1, column=0)

passwordEntry = tk.Entry(app)
passwordEntry.grid(row=1, column=1)

# Submit Button
submitButton = tk.Button(app, text='Submit', command=check_credentiials)
submitButton.grid(row=2, column=0)
app.mainloop()

