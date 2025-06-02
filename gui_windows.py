from tkinter import *

# widget: GUI elements:buttons,textboxes,labels,images
# windows: serves as a container to hold or contain these widgets

window=Tk() # instantiate an instance of a window
window.geometry("420x420") #determining window size
window.title("Allan Otieno first GUI program")

# creating photo image from png
icon = PhotoImage(file="logo.png")  # ✅ Capital P
window.iconphoto(True, icon)

#changing background color of the window
window.config(background="#121720")

window.mainloop() #shows the window on computer screen and also listen for events


