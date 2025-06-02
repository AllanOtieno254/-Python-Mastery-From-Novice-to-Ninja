# buttons:you click it then it does stuff
from itertools import count
from tkinter import *

count = 0  # simple counter

def click():
    global count
    count += 1
    print(f"You clicked the button {count} times")

window = Tk()
window.geometry("500x500")
window.config(background="#121720")
window.title("Creating Button")

photo = PhotoImage(file="logo.png")  # Ensure this file exists in your folder

button = Button(window,
                text="Click Me",
                command=click,
                font=("Times New Roman", 20, "bold"),
                fg="green",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE,
                image=photo,
                compound="bottom")
button.pack()
button.place(x=200, y=200)

window.mainloop()
