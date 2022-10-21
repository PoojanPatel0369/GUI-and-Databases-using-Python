'''
Question:
Create a list of radio buttons that the user clicks and displays the selected
radio button.
'''

from tkinter import *

root = Tk()
root.title('Radiobuttons')
root.iconbitmap('S:\Programming Practice\GitHub\GUI-and-Databases-using-Python\Picture Library\Logo.ico')
root.geometry("300x400+600+150")

TOPPINGS = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroon", "Mushroon"),
    ("Panner", "Panner"),
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, topping in TOPPINGS:
    Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)
def clicked(value):
    myLabel = Label(root, text=value).pack()

myButton = Button(root, text="Click Me!", command=lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop()
