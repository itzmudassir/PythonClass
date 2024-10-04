import tkinter as tk

app = tk.Tk()
app.title('RadioButton')
app.geometry('300x200')

gender = tk.IntVar()

genderDict = {1: 'Male', 2: 'Female', 3: 'Other'}

def showSelection():
    selectedOption = genderDict.get(gender.get(), 'Unknown')
    radioLabel.config(text=f"Selected option: {selectedOption}")

male = tk.Radiobutton(text='Male', variable=gender, value = 1, command=showSelection)
male.pack(pady=10)

female = tk.Radiobutton(text='Female', variable=gender, value = 2, command=showSelection)
female.pack(pady=10)

other = tk.Radiobutton(text='Other', variable=gender, value = 3, command=showSelection)
other.pack(pady=10)

radioLabel = tk.Label(app, text='Please select any option.')
radioLabel.pack(pady=10)

app.mainloop()