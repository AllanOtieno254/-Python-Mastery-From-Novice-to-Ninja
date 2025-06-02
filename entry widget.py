# entry widget/box:text box that accepts a single line of user input

from tkinter import *
from unittest.mock import right


def submit():
    user_name=entry.get()
    print(f"Hello {user_name}")
    print("submission was succesful")

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1,END)

window=Tk()

entry=Entry(window,font=("Arial",14,"bold"),bg="black",fg="red",show="*")
entry.pack(side=LEFT)
entry.place(x=200,y=300)

submit_button=Button(window,text="Submit",font=("Arial",22,"bold"),bg="light green",command=submit)
submit_button.pack(side=RIGHT)
submit_button.place(x=450,y=290)

delete_button=Button(window,text="Delete",font=("Arial",22,"bold"),bg="light green",command=delete)
delete_button.pack(side=RIGHT)
delete_button.place(x=600,y=290)

backspace_button=Button(window,text="backspace",font=("Arial",22,"bold"),bg="light green",command=backspace)
backspace_button.pack(side=RIGHT)
backspace_button.place(x=750,y=290)


window.geometry("500x500")


window.title("entry box")
window.config(background="#121621")
window.mainloop()