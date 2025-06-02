from cProfile import label
from tkinter import  *

#label: an area widget that holds text and/or an image within a window

window=Tk()

photo=PhotoImage(file="logo.png")

window.geometry("650x650")
window.title("working on label widgets")
window.config(background="#245161")

label=Label(window,text="Welcome to the label section in GUI",font=("Times New Roman",20,"bold"),image=photo,compound="bottom",bg="#121720",fg="white")
label.pack()

label=Label(window,text="changing label positiion",font=("Arial"),fg="#00FF00",bg="black")
label.place(x=250,y=150)
window.mainloop()