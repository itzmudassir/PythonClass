import tkinter as tk
from time import strftime

# Create the main app
app = tk.Tk()
app.title("Digital Clock")
app.geometry("400x200")

# Function to update the time
def update_time():
    current_time = strftime("%H:%M:%S")  # Get current time in HH:MM:SS format
    time_label.config(text=current_time)  # Update the label with current time
    time_label.after(1000, update_time)   # Call this function again after 1000 ms (1 second)

# Create a label to display the time
time_label = tk.Label(app, font=("Arial", 48), bg="black", fg="white")
time_label.pack(pady=20)


# Call the update_time function initially
update_time()

# Run the application
app.mainloop()
