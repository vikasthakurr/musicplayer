import pygame
from tkinter import filedialog
from tkinter import *
import tkinter as tk
print vikas
root = tk.Tk()
root.title('Music Player')
root.geometry('500x500')
root.config(bg='white')
pygame.mixer.init()
song_list = tk.Listbox(root, width=60, bg='black', fg='white')
song_list.pack(pady=20)
