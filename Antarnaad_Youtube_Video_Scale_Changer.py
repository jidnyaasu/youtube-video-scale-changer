from tkinter import *
from tkinter import filedialog

from main import main

root = Tk()
root.title('Antarnaad Youtube Video Scale Changer')
root.geometry('600x400+650+300')


def on_click():
    complete = main(url.get(), scale_change.get(), output_folder.get())
    Label(root, text=complete).place(anchor=CENTER, relx=.5, rely=.8)


def paste():
    clipboard = root.clipboard_get()
    url.insert(0, clipboard)


def ask_folder():
    folder = filedialog.askdirectory() + '/'
    output_folder.insert(0, folder)


Label(root, text="Please paste YouTube Video Link here :  ").place(anchor=CENTER, relx=.3, rely=.1)

# url textbox
url = Entry(root, width=50, borderwidth=3)
url.pack()
url.place(anchor=CENTER, relx=.4, rely=.2)
# Paste button
Button(root, text="Paste", command=paste).place(anchor=CENTER, relx=.9, rely=.2)

# Output folder textbox
Label(root, text="Please select output folder :  ").place(anchor=CENTER, relx=.23, rely=.3)
output_folder = Entry(root, width=50, borderwidth=3)
output_folder.pack()
output_folder.place(anchor=CENTER, relx=.4, rely=.4)
# Select folder button
Button(root, text="Select Folder", command=ask_folder).place(anchor=CENTER, relx=.9, rely=.4)

# Select pitch change step
Label(root, text="Please select number of steps to change pitch :  ").place(anchor=CENTER, relx=.5, rely=.5)
scale_change = Entry(root, width=20, borderwidth=3)
scale_change.pack()
scale_change.place(anchor=CENTER, relx=.5, rely=.6)

# Download button
Button(root, text="Download", command=on_click).place(anchor=CENTER, relx=.5, rely=.7)

# Author info
author = Label(root, text="Software by: Saurabh Joshi")
author.place(anchor=CENTER, relx=.5, rely=.9)

root.mainloop()
