'''
Question:
Create a root window that lets the user open another window.
'''

from tkinter import *

root = Tk()
root.title('First Window')
root.iconbitmap('S:\Programming Practice\GitHub\GUI-and-Databases-using-Python\Picture Library\Logo.ico')
root.geometry("300x50+650+150")

def open():
    top = Toplevel()
    top.title('Second Window')
    top.iconbitmap('S:\Programming Practice\GitHub\GUI-and-Databases-using-Python\Picture Library\Logo.ico')
    top.geometry("300x50+650+250")
    btn2 = Button(top, text="Close Window", command=top.destroy).pack()

btn = Button(root, text="Open Second Window", command=open).pack()    

root.mainloop()
