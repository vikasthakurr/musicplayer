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


