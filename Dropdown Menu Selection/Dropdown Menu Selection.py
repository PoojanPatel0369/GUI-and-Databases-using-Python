'''
Question:
Design a Dropdown Menu containing the days of a week and display the selction
by the user.
'''

from tkinter import *

root = Tk()
root.title('Dropdown Menu Selection')
root.iconbitmap('S:\Python\Graphical User Interface (GUI) and Databases with Python\Picture Library\Logo.ico')
root.geometry("400x400")

def show():
    myLabel = Label(root, text=clicked.get()).pack()

options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()
