import os
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter.font import Font


class DownloaderGui:

    def __init__(self, root, title):
        self.root = root
        self.root.title(title)
        self.root.configure(bg="#FCF2D8")
        self.root.config(padx=50, pady=20)

        # url textbox
        self.url_label = Label(self.root, text="Please paste Video Link here :  ", bg="#FCF2D8")
        self.url_label.grid(column=0, row=0, columnspan=2, pady=(0, 5))
        self.url = Entry(self.root, width=50, borderwidth=3, bg="alice blue")
        self.url.grid(column=0, row=1, columnspan=2, pady=5)

        # Paste button
        self.paste_button = Button(self.root, text="Paste", command=self.paste, bg="pink")
        self.paste_button.grid(column=0, row=2, columnspan=2, pady=5)

        # Output folder textbox
        self.output_folder_label = Label(self.root, text="Please select output folder :  ", bg="#FCF2D8")
        self.output_folder_label.grid(column=0, row=3, columnspan=2, pady=(20, 5))
        self.output_folder = Entry(self.root, width=50, borderwidth=3, bg="alice blue")
        self.output_folder.grid(column=0, row=4, columnspan=2, pady=5)

        # Defaulting output folder to Videos directory
        if os.name == "nt":
            self.videos_directory = os.path.expanduser("~") + "\\Videos\\"
        else:
            self.videos_directory = os.path.expanduser("~") + "/Videos/"
        self.output_folder.insert(0, self.videos_directory)

        # Select folder button
        self.select_folder_button = Button(self.root, text="Select Folder", command=self.ask_folder, bg="pink")
        self.select_folder_button.grid(column=0, row=5, columnspan=2, pady=5)

        # Pitch change step
        self.select_pitch_change_label = Label(
            self.root, text="Please select number of steps to change pitch :  ", bg="#FCF2D8")
        self.select_pitch_change_label.grid(column=0, row=6, columnspan=2, pady=(20, 5))
        zero = IntVar(root)
        zero.set(0)
        self.scale_change = Spinbox(from_=-6, to=6, width=5, textvariable=zero)
        self.scale_change.grid(column=0, row=7, columnspan=2, pady=5)

        # Download button
        self.download_button = Button(
            self.root,
            text="",
            bg="light green",
        )
        self.download_button.grid(column=0, row=8, columnspan=2, pady=5)

        # Status Message
        self.status_message = Label(self.root, text="", bg="#FCF2D8")
        self.status_message.grid(column=0, row=9, pady=(5, 10), columnspan=2)

        # Author info
        author_font = Font(family="Helvetica", weight="bold")
        author = Label(
            self.root, text="Software by: Saurabh Joshi", fg="maroon", bg="#FCF2D8", font=author_font
        )
        author.grid(column=0, row=10, columnspan=2, pady=(10, 0))

    def paste(self):
        clipboard = self.root.clipboard_get()
        self.url.delete(0, tkinter.END)
        self.url.insert(0, clipboard)

    def ask_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            if os.name == "nt":
                folder += "\\"
            else:
                folder += "/"
            self.output_folder.delete(0, tkinter.END)
            self.output_folder.insert(0, folder)
