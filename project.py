import tkinter as tk
from tkinter import *
from tkinter import filedialog
import pygame
root = tk.Tk()
root.title('Music Player')
root.geometry('500x500')
root.config(bg='white')
pygame.mixer.init()
song_list = tk.Listbox(root, width=60, bg='black', fg='white')
song_list.pack(pady=20)


def add_song():
    songs = filedialog.askopenfilenames(
        initialdir='D:\music playr', title='Add Music', filetypes=(('mp3 Files', '*.mp3'),))
    for song in songs:
        songs = song.replace('D:\music playr', '')
    song_list.insert(END, songs)


def play_song():
    song = song_list.get(ACTIVE)
    song = f'D:\music playr{song}'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)


def stop_song():
    pygame.mixer.music.stop()
    song_list.selection_clear(ACTIVE)


global paused
paused = False


def pause_song():
    global paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True


def play_next_song():
    next_song = song_list.curselection()
    next_song = next_song[0]+1
    song = song_list.get(next_song)
    song = f'D:\music playr\{song}'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    song_list.selection_clear(0, END)
    song_list.selection_set(next_song, last=None)


def play_previous_song():
    next_song = song_list.curselection()
    next_song = next_song[0]-1
    song = song_list.get(next_song)
    song = f'D:\music playr{song}'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    song_list.selection_clear(0, END)
    song_list.selection_set(next_song, last=None)


frame = tk.Frame(root, bg='white')
frame.pack()
play_button = tk.Button(frame, text='Play', padx=10,
                        pady=10, command=play_song)
pause_button = tk.Button(frame, text='Pause', padx=10,
                         pady=10, command=pause_song)
stop_button = tk.Button(frame, text='Stop', padx=10,
                        pady=10, command=stop_song)
next_button = tk.Button(frame, text='Next', padx=10,
                        pady=10, command=play_next_song)
previous_button = tk.Button(
    frame, text='Previous', padx=10, pady=10, command=play_previous_song)

play_button.pack(side=LEFT, padx=5)
pause_button.pack(side=LEFT, padx=5)
stop_button.pack(side=LEFT, padx=5)
next_button.pack(side=LEFT, padx=5)
previous_button.pack(side=LEFT, padx=5)

add_song_btn = tk.Button(root, text='Add Songs',
                         padx=10, pady=3, command=add_song)
add_song_btn.pack(pady=20)
root.mainloop()
