import tkinter as tk

app = tk.Tk()
app.geometry("300x200")
app.title("Intro")

def userData():
    user = userEntry.get().strip()
    if user:
        userLabel.config(text=user)
    else:
        userLabel.config(text='try again')
        
    
    


userLabel = tk.Label(app, text='Welcome!')
userLabel.pack(pady=10)

userEntry = tk.Entry(app)
userEntry.pack(pady=10)

submitButton = tk.Button(app, text="Sumbit", command=userData)
submitButton.pack(pady=10)


app.mainloop()