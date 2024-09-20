import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Greeting App")
root.geometry("300x200")

# Function to update the label
def update_label():
    name = name_entry.get()
    name = name.capitalize()
    if name.strip():
        greeting_label.config(text=f"Hello, {name}!")
    else:
        greeting_label.config(text="Please enter your name!")

# Greeting label
greeting_label = tk.Label(root, text="Hello, User!", font=("Arial", 14))
greeting_label.pack(pady=10)

# Entry field for name
name_entry = tk.Entry(root, width=20)
name_entry.pack(pady=5)

# Submit button
submit_button = tk.Button(root, text="Submit", command=update_label)
submit_button.pack(pady=5)

# Run the application
root.mainloop()
