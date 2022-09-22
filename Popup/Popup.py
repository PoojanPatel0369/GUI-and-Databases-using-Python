'''
Question:
Create a root window that lets the user explore the various types of message box
popups.
'''

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Types of Popups')
root.iconbitmap('S:\Python\Graphical User Interface (GUI) and Databases with Python\Picture Library\Logo.ico')
root.geometry("280x160+620+150")

#Types of message boxes: showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup1():
    response = messagebox.showinfo("Info Popup", "Hello World!")
Button(root, text="Info Popup", command=popup1).grid(row=0, column=1, columnspan=1, padx=80)
    
def popup2():
    response = messagebox.showwarning("Warning Popup", "Hello World!")
Button(root, text="Warning Popup", command=popup2).grid(row=1, column=1, columnspan=1, padx=80)
    
def popup3():
    response = messagebox.showerror("Error Popup", "Hello World!")
Button(root, text="Error Popup", command=popup3).grid(row=2, column=1, columnspan=1, padx=80)

def popup4():
    response = messagebox.askquestion("Question Popup", "Hello World!")
Button(root, text="Question Popup", command=popup4).grid(row=3, column=1, columnspan=1, padx=80)

def popup5():
    response = messagebox.askokcancel("Ok/Cancel Popup", "Hello World!")
Button(root, text="Ok/Cancel Popup", command=popup5).grid(row=4, column=1, columnspan=1, padx=80)

def popup6():
    response = messagebox.askyesno("Yes/No Popup", "Hello World!")
Button(root, text="Yes/No Popup", command=popup6).grid(row=5, column=1, columnspan=1, padx=80)

root.mainloop()
