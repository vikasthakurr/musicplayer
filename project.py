# Code for music player for desktop using python GUI by Vikas kumar (12008810)


import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

musicplayer = tkr.Tk()

musicplayer.title("My gana")

musicplayer.geometry("450x350")

directory = askdirectory()


os.chdir(directory)

songlist = os.listdir()

# Creating the playlist
playlist = tkr.Listbox(musicplayer, font="Cambria 14 bold",
                       bg="white", selectmode=tkr.SINGLE)

# Adding songs from songlist to playlist
for item in songlist:
    pos = 0
    playlist.insert(pos, item)
    pos = pos+1


pygame.init()
pygame.mixer.init()

# Function for Play button


def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()

# Function fo Stop button


def exitmusicplayer():
    pygame.mixer.music.stop()

# Function for Pause button


def pause():
    pygame.mixer.music.pause()

# Function for Resume/Unpause button


def resume():
    pygame.mixer.music.resume()


# Creating Buttons
Button_Play = tkr.Button(musicplayer, height=3, width=5, text="Play",
                         font="Cambria 14 bold", command=play, bg="lime green", fg="black")
Button_Stop = tkr.Button(musicplayer, height=3, width=5, text="Stop",
                         font="Cambria 14 bold", command=exitmusicplayer, bg="red", fg="black")
Button_Pause = tkr.Button(musicplayer, height=3, width=5, text="Pause",
                          font="Cambria 14 bold", command=pause, bg="yellow", fg="black")
Button_Resume = tkr.Button(musicplayer, height=3, width=5, text="Resume",
                           font="Cambria 14 bold", command=resume, bg="lime green", fg="black")
Button_Play.pack(fill="x")
Button_Stop.pack(fill="x")
Button_Pause.pack(fill="x")
Button_Resume.pack(fill="x")

playlist.pack(fill="both", expand="yes")

var = tkr.StringVar()
songtitle = tkr.Label(musicplayer, font="Cambria 12 bold", textvariable=var)
songtitle.pack()
musicplayer.mainloop()
