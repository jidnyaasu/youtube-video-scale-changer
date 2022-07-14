import _tkinter
import os.path
import tkinter
from tkinter import *
from threading import Thread
from tkinter import filedialog

from main import main

root = Tk()
root.title('Antarnaad Youtube Video Scale Changer')
root.geometry('600x400+650+300')


def download():
    if url.get():
        thr = Thread(target=main, args=[status_message, url.get(), scale_change.get(), output_folder.get()])
        thr.start()
    else:
        status_message.config(text="Please paste/enter video link", fg="crimson")


def paste():
    try:
        clipboard = root.clipboard_get()
        url.delete(0, tkinter.END)
        url.insert(0, clipboard)
    except _tkinter.TclError:
        pass


def ask_folder():
    folder = filedialog.askdirectory() + '/'
    output_folder.delete(0, tkinter.END)
    output_folder.insert(0, folder)


# url label
url_label = Label(root, text="Please paste YouTube Video Link here :  ")
url_label.pack(expand=True)

# url textbox
url = Entry(root, width=50, borderwidth=3)
url.pack(expand=True)
try:
    if root.clipboard_get().__contains__("youtube.com"):
        url.insert(0, root.clipboard_get())
except _tkinter.TclError:
    pass

# Paste button
paste_button = Button(root, text="Paste", command=paste)
paste_button.pack(expand=True)

# Output folder textbox
output_folder_label = Label(root, text="Please select output folder :  ")
output_folder_label.pack(expand=True)
output_folder = Entry(root, width=50, borderwidth=3)
output_folder.pack(expand=True)

# Defaulting output folder to Videos directory
videos_directory = os.path.expanduser("~") + "/Videos/"
output_folder.insert(0, videos_directory)

# Select folder button
select_folder_button = Button(root, text="Select Folder", command=ask_folder)
select_folder_button.pack(expand=True)

# Select pitch change step
select_pitch_change_label = Label(root, text="Please select number of steps to change pitch :  ")
select_pitch_change_label.pack(expand=True)
zero = IntVar(root)
zero.set(0)
scale_change = Spinbox(from_=-6, to=6, width=5, textvariable=zero)
scale_change.pack(expand=True)

# Download button
download_button = Button(root, text="Download", command=download)
download_button.pack(expand=True)

# Status message
status_message = Label(root, text="")
status_message.pack(expand=True)

# Author info
author = Label(root, text="Software by: Saurabh Joshi")
author.pack(expand=True)

root.mainloop()
