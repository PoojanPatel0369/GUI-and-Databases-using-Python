'''
Question:
Create an input box that asks the user's name and greet them.
'''

from tkinter import *

root = Tk()
root.title('Input Box')
root.iconbitmap('S:\Programming Practice\GitHub\GUI-and-Databases-using-Python\Picture Library\Logo.ico')
root.geometry("400x100+550+200")

e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter your name: ")

def myClick():
    hello = 'Hello ' + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text="Enter your name!", command = myClick)
myButton.pack()

root.mainloop()
























