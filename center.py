import tkinter as tk

app = tk.Tk()
app.title('Center')
app.geometry('300x200')

# Create a label widget
label = tk.Label(app, text='Hello, World!')
label.grid(row=0, column=0)

# Center the label widget
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

app.mainloop()