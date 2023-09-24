from tkinter import *
import tkinter as tk 
from tkinter import ttk, filedialog
from pygame import mixer
import os
import random  # for shuffle

root = Tk()

root.title("Music Player")
root.geometry('920x670+290+85')
root.configure(bg="#0f1a2b")


mixer.init()

# Define a global list to store the playlist
playlist = []

def open_folder():
    global playlist  # Access the global playlist variable
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.append(song)  # Add the song to the playlist
                play_list.insert(END, song)

def play_song():
    music_name = play_list.get(ACTIVE)
    mixer.music.load(music_name)
    mixer.music.play()
    music.config(text=music_name[0:-4])

def next_song():
    global playlist  # Access the global playlist variable
    current_song = play_list.get(ACTIVE)
    current_index = playlist.index(current_song)
    next_index = (current_index + 1) % len(playlist)  # Circular playlist
    play_list.selection_clear(0, END)
    play_list.activate(next_index)
    play_list.selection_set(next_index)
    play_song()

def prev_song():
    global playlist  # Access the global playlist variable
    current_song = play_list.get(ACTIVE)
    current_index = playlist.index(current_song)
    prev_index = (current_index - 1) % len(playlist)  # Circular playlist
    play_list.selection_clear(0, END)
    play_list.activate(prev_index)
    play_list.selection_set(prev_index)
    play_song()

def repeat_toggle():
    global repeat_var
    if repeat_var.get() == 1:
        mixer.music.set_repeat(1)  # Repeat enabled
    else:
        mixer.music.set_repeat(0)  # Repeat disabled

def shuffle_playlist():
    global playlist
    random.shuffle(playlist)
    play_list.delete(0, END)  # Clear the current list
    for song in playlist:
        play_list.insert(END, song)

# Icon
image_icon = PhotoImage(file='src/logo.png')
root.iconphoto(False, image_icon)

# Top
Top = PhotoImage(file="src/top.png")
Label(root, image=Top, bg="#0f1a2b").pack()

# Logo
Logo = PhotoImage(file="src/logo.png")
Label(root, image=Logo, bg="#0f1a2b").place(x=65, y=115)

# Buttons
play_button = PhotoImage(file="src/play.png")
Button(root, image=play_button, bg="#0f1a2b", bd=0, command=play_song).place(x=100, y=400)

stop_button = PhotoImage(file="src/stop.png")
Button(root, image=stop_button, bg="#0f1a2b", bd=0, command=mixer.music.stop).place(x=30, y=500)

resume_button = PhotoImage(file="src/resume.png")
Button(root, image=resume_button, bg="#0f1a2b", bd=0, command=mixer.music.unpause).place(x=115, y=500)

pause_button = PhotoImage(file="src/pause.png")
Button(root, image=pause_button, bg="#0f1a2b", bd=0, command=mixer.music.pause).place(x=200, y=500)

previous_button = PhotoImage(file="src/rsz_previous.png")  # Add your image file
Button(root, image=previous_button, bg="#0f1a2b", bd=0, command=prev_song).place(x=30, y=570)  # Adjusted placement

next_button = PhotoImage(file="src/next.png")
Button(root, image=next_button, bg="#0f1a2b", bd=0, command=next_song).place(x=200, y=570)  # Adjusted placement

# Label
music = Label(root, text="", font=("arial", 15), fg='white', bg="#0f1a2b")
music.place(x=150, y=340, anchor="center")

# Music Menu
Menu = PhotoImage(file="src/menu.png")
Label(root, image=Menu, bg="#0f1a2b").pack(padx=10, pady=50, side=RIGHT)

# Music Frame
music_frame = Frame(root, bd=2, relief=RIDGE)
music_frame.place(x=330, y=350, width=560, height=250)

# Buttons
Button(root, text="Open Folder", width=15, height=2, font=('arial', 10, "bold"), fg="white", bg="#21b3de", command=open_folder).place(x=330, y=300)
Button(root, text="Repeat", width=10, height=2, font=('arial', 10, "bold"), fg="white", bg="#21b3de", command=repeat_toggle).place(x=460, y=300)
Button(root, text="Shuffle", width=10, height=2, font=('arial', 10, "bold"), fg="white", bg="#21b3de", command=shuffle_playlist).place(x=590, y=300)

# Scrollbar and Playlist
scroll = Scrollbar(music_frame)
play_list = Listbox(music_frame, width=100, font=("arial", 10), bg="#333333", fg="grey", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=scroll.set)
scroll.config(command=play_list.yview)
scroll.pack(side=RIGHT, fill=Y)
play_list.pack(side=LEFT, fill=BOTH)

root.mainloop()
