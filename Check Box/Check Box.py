'''
Question:
Create a simple Check Box.
'''

from tkinter import *

root = Tk()
root.title('Check Box')
root.iconbitmap('S:\Programming Practice\GitHub\GUI-and-Databases-using-Python\Picture Library\Logo.ico')
root.geometry("300x100")

def show():
    myLabel = Label(root, text=var.get()).pack()

var = StringVar()

c = Checkbutton(root, text="Check this box, I dare you!", variable=var, onvalue="Pizza", offvalue="Burger")
c.deselect()
c.pack()

root.mainloop()
