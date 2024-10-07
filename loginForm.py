import tkinter as tk
from tkinter import messagebox

def submit():
    username = entry_username.get()
    password = entry_password.get()
    language = []
    if var_english.get():
        language.append("English")
    if var_spanish.get():
        language.append("Spanish")
    gender = var_gender.get()

    messagebox.showinfo("Submission", f"Username: {username}\nPassword: {password}\nLanguage: {', '.join(language)}\nGender: {gender}")

# Create the main window
root = tk.Tk()

width = 400 # Width 
height = 400 # Height
 
screen_width = root.winfo_screenwidth()  # Width of the screen
screen_height = root.winfo_screenheight() # Height of the screen
 
# Calculate Starting X and Y coordinates for Window
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
 
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.title("Login Form")

# Heading
heading = tk.Label(root, text="Login Form", font=("Arial", 20))
heading.pack(pady=10)

# Frame for username
frame_username = tk.Frame(root)
frame_username.pack(pady=5)

label_username = tk.Label(frame_username, text="Username:")
label_username.pack(side='left', padx=5)

entry_username = tk.Entry(frame_username)
entry_username.pack(side='left', padx=5)

# Frame for password
frame_password = tk.Frame(root)
frame_password.pack(pady=5)

label_password = tk.Label(frame_password, text="Password:")
label_password.pack(side='left', padx=5)

entry_password = tk.Entry(frame_password, show="*")
entry_password.pack(side='left', padx=5)

# Language checkboxes
var_english = tk.BooleanVar()
var_spanish = tk.BooleanVar()

label_language = tk.Label(root, text="Select Language:")
label_language.pack(pady=5)

# Frame for checkboxes
frame_language = tk.Frame(root)
frame_language.pack(pady=5)

checkbox_english = tk.Checkbutton(frame_language, text="English", variable=var_english)
checkbox_english.pack(side='left', padx=10)

checkbox_spanish = tk.Checkbutton(frame_language, text="Spanish", variable=var_spanish)
checkbox_spanish.pack(side='left', padx=10)

# Gender radio buttons
var_gender = tk.StringVar(value="Male")

label_gender = tk.Label(root, text="Select Gender:")
label_gender.pack(pady=5)

# Frame for radio buttons
frame_gender = tk.Frame(root)
frame_gender.pack(pady=5)

radio_male = tk.Radiobutton(frame_gender, text="Male", variable=var_gender, value="Male")
radio_male.pack(side='left', padx=10)

radio_female = tk.Radiobutton(frame_gender, text="Female", variable=var_gender, value="Female")
radio_female.pack(side='left', padx=10)

radio_other = tk.Radiobutton(frame_gender, text="Other", variable=var_gender, value="Other")
radio_other.pack(side='left', padx=10)

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack(pady=20)

# Run the application
root.mainloop()
