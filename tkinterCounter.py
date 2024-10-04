import tkinter as tk

# Create main window
window = tk.Tk()
window.title("Simple Counter")
window.geometry("300x200")

# Counter value variable
counter = 0

# Function to increment the counter
def increment():
    global counter
    counter += 1
    counter_label.config(text=str(counter))

# Function to decrement the counter
def decrement():
    global counter
    counter -= 1
    counter_label.config(text=str(counter))
    
# Label to display the counter value
counter_label = tk.Label(window, text=str(counter), font=("Arial", 24))
counter_label.pack(pady=20)


# Increment button
increment_button = tk.Button(window, text="Increment", command=increment)
increment_button.pack(side="left", padx=20)

# Decrement button
decrement_button = tk.Button(window, text="Decrement", command=decrement)
decrement_button.pack(side="right", padx=20)

# Run the application
window.mainloop()
