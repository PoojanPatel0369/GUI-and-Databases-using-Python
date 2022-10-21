'''
Question:
Use sliders to make the size of the root window variable using GUI.
'''

from tkinter import *

root = Tk()
root.title('Sliders')
root.iconbitmap('S:\Programming Practice\GitHub\GUI-and-Databases-using-Python\Picture Library\Logo.ico')
root.geometry("300x200")

def slide():
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

vertical = Scale(root, from_=200, to=600)
vertical.pack()

horizontal = Scale(root, from_=300, to=700, orient=HORIZONTAL)
horizontal.pack()

my_label = Label(root, text=horizontal.get()).pack()
my_btn = Button(root, text="Click Me!", command=slide).pack()

root.mainloop()
