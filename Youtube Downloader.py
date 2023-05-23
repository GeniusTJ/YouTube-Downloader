from ctypes import resize
from importlib.resources import path
from select import select
from tkinter import *
from tkinter import filedialog
from turtle import Screen, left, title
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube

import shutil


# Functions


def select_path():
    # allows user to select a path from the explorer
    path = filedialog.askdirectory()
    path_label.config(text=path)


def download_file():
    # get usr path
    get_link = link_field.get()
    # get selected path
    user_path = path_label.cget("text")
    screen.title('Downloading...')

    # Download Video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    # move file to selected directory
    shutil.move(mp4_video, user_path)
    screen.title('Download Complete! Download Another File... ')


screen = Tk()
title = screen.title('Youtube Downloader')
canvas = Canvas(screen, width=500, height=500)
canvas.pack(padx=20, pady=20)

# image logo
logo_img = PhotoImage(file="YouTube-Logo.png")

# resize
logo_img = logo_img.subsample(10, 10)
canvas.create_image(250, 80, image=logo_img)

# Link field
link_field = Entry(screen, width=50)
link_label = Label(screen, text="Enter Download Link:",
                   font=('Arial', 15))

# Select path for saving the file
path_label = Label(screen, text="Select Path For Download",
                   font=('Arial', 15))
select_btn = Button(screen, text="Select", command=select_path)

# Add to window
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)


link_field.pack(side=RIGHT)
#link_label.pack(padx=10, pady=0)


# Add widgets to window
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)

# Download btns
download_btn = Button(screen, text="Download File", command=download_file)
# add to canvas
canvas.create_window(250, 390, window=download_btn)


screen.mainloop()
