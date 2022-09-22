'''
Question:
Create a dialog box that lets the user open images from a folder.
'''

from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()
root.title('Dialog Box')
root.geometry("260x278+650+300")
root.iconbitmap('S:\Python\Graphical User Interface (GUI) and Databases with Python\Picture Library\Logo.ico')

def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir='S:\Python\Graphical User Interface (GUI) and Databases with Python\Picture Library', title="Select A File", filetypes=(("jpg files", "*.jpg"),("all files", "*.*")))
    my_label = Label(root, text=root.filename)
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image)
    my_image_label.grid(row=2, column=1, columnspan=1)

my_btn = Button(root, text="Open File",width=10,height=2, command=open)#.pack()
close_btn = Button(root, text="Exit Program",width=10,height=2, command=root.destroy)#.pack()

my_btn.grid(row=0, column=1, columnspan=1, padx=90)
close_btn.grid(row=1, column=1, columnspan=1, padx=90)


root.mainloop()
