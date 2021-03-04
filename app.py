from tkinter import *
from tkinter import messagebox

user_input = ""

def check_text():
    global user_input
    if len(text.get(1.0, END)) > 1:
        if text.get(1.0, END) == user_input: 
            text.delete(1.0, END)
            text.config(bg="#d6c8ff", state=DISABLED)
            canvas.itemconfig(title, text = "Time's up! You haven't write for 5 seconds.")
            canvas.itemconfig(subtitle, text = "")
            again = messagebox.askretrycancel("Text is gone!", "Do you want to type again?")
            if again:
                canvas.itemconfig(title, text="Welcome to the disappearing text desktop app!")
                canvas.itemconfig(subtitle, text="\nIf you stop writing for more than 5 seconds, your text will disappear")
                user_input = ""
                text.config(bg="#fef0ff", state=NORMAL)
            else:
                window.quit()
        user_input = text.get(1.0, END) 
    window.after(5000, check_text)


window = Tk()
window.title("Disappearing Text")

canvas = Canvas(width=720, height=140, bg="#d6c8ff")

title = canvas.create_text(360, 30, text="Welcome to the disappearing text desktop app!",
                           font=("Arial", 22, "bold"))
subtitle = canvas.create_text(350, 55, text="\nIf you stop writing for more than 5 seconds, your text will disappear", font=("Arial", 13))
canvas.pack()

text = Text(window, height=30, width=80, bg="#fef0ff", font = "Helvetica")
text.pack()
text.focus()

check_text()

window.mainloop()