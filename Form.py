import os
from main import play_song, stop_song, continue_song, play_next, play_last
from tkinter import *
import tkinter.ttk as ttk
from threading import Thread
import pygame

root = Tk()
root.geometry("400x250")
os.environ['Sp_VIDEO_WINDOW_POS'] = "100, 100"
root.title('Audio-player')


def play_Btn_on_click():
    if play_Btn['text'] == 'Play':
        play_Btn['text'] = '||'
        play_song(music_name, progress_bar)
    elif play_Btn['text'] == '||':
        play_Btn['text'] = '|>'
        stop_song(music_name)
    else:
        play_Btn['text'] = '||'
        continue_song(music_name)

  
play_Btn = Button(root, text="Play", command=lambda: play_Btn_on_click())
play_Btn.grid(row=3, column=2)

next_song_Btn = Button(root, text="Next", command=lambda: play_next(music_name, progress_bar, play_Btn))
next_song_Btn.grid(row=3, column=3)

last_song_Btn = Button(root, text="Last", command=lambda: play_last(music_name, progress_bar, play_Btn))
last_song_Btn.grid(row=3, column=1)

music_name = Label(text='Выберите песню')
music_name.grid(row=1, column=2)

progress_bar = ttk.Progressbar(root, mode="determinate")
progress_bar.grid(row=2, column=2)

if 'normal' != root.state():
    root.mainloop()
if pygame.mixer.music.get_busy():
    progress_bar['value'] = pygame.mixer.music.get_pos()
for event in pygame.event.get():
    if event.type == pygame.USEREVENT:
        play_next(music_name, progress_bar)
