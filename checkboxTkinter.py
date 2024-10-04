import tkinter as tk


app = tk.Tk()
app.title('Simple Checkbox')
app.geometry('300x200')

var1 = tk.IntVar()

def showSelection():
    if var1.get() == 1:
        label.config(text='Checkbox is Checked.')
    else:
        label.config(text='Checkbox is Unchecked.')

checkbox = tk.Checkbutton(app, text= 'Check me!', variable=var1, command=showSelection)
checkbox.pack(pady=20)

label = tk.Label(app, text='Checkbox is Unchecked.')
label.pack(pady=20)

app.mainloop()