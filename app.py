from threading import Thread
from tkinter import *

from main import main
from ui import DownloaderGui

root = Tk()
title = "Antarnaad Scale Changer"
app = DownloaderGui(root, title)


def download(local_app):
    if local_app.url.get():
        thr = Thread(target=main,
                     args=[local_app.status_message, local_app.download_button, local_app.url.get(),
                           local_app.scale_change.get(), local_app.output_folder.get()])
        thr.start()
    else:
        local_app.status_message.config(text="Please paste video url", fg="red")


app.download_button.config(text="Download", command=lambda: download(app))

root.mainloop()
