'''
Question:
Build an Image Viewer App With Python and Tkinter
'''

from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Image Viewer App')
root.iconbitmap('S:\Python\Graphical User Interface (GUI) and Databases with Python\Picture Library\Logo.ico')

my_img1 = ImageTk.PhotoImage(Image.open("S:\Python\Graphical User Interface (GUI) and Databases with Python\Picture Library\A.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("S:\Python\Graphical User Interface (GUI) and Databases with Python\Picture Library\B.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("S:\Python\Graphical User Interface (GUI) and Databases with Python\Picture Library\C.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("S:\Python\Graphical User Interface (GUI) and Databases with Python\Picture Library\D.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("S:\Python\Graphical User Interface (GUI) and Databases with Python\Picture Library\E.jpg"))
my_img6 = ImageTk.PhotoImage(Image.open("S:\Python\Graphical User Interface (GUI) and Databases with Python\Picture Library\F.jpg"))
my_img7 = ImageTk.PhotoImage(Image.open("S:\Python\Graphical User Interface (GUI) and Databases with Python\Picture Library\G.jpg"))
my_img8 = ImageTk.PhotoImage(Image.open("S:\Python\Graphical User Interface (GUI) and Databases with Python\Picture Library\H.jpg"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6, my_img7, my_img8]

status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: forward(image_number-1))

    if image_number == 8:
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: forward(image_number-1))

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

button_back = Button(root, text="<<", command=back, state=DISABLED)
button_forward = Button(root, text=">>", command=lambda: forward(2))
button_exit = Button(root, text="Exit Program", command=root.destroy)

button_back.grid(row=1, column=0)
button_forward.grid(row=1, column=2, pady=10)
button_exit.grid(row=1, column=1)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()











