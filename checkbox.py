from tkinter import  *

def display():
    if(x.get()==1):
        print("you agree")
    else:
        print("you dont agree")

window=Tk()

x=IntVar()

check_button=Checkbutton(window,text="i agree to terms and condition",variable=x,onvalue=1,offvalue=0,command=display,font=("Arial,bold"),fg="green",bg="black")
check_button.pack()

window.geometry("600x600")
window.config(background="#121720")
window.mainloop()