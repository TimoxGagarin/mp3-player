import os
import pygame
import time
from tkinter import *
from playsound import playsound 

pygame.init()
songs = os.listdir('songs')
song_number = 0


def play_song(label: Label, pb):
    pygame.mixer.Sound('songs/' + songs[song_number]).play()
    pb['maximum'] = pygame.mixer.Sound('songs/' + songs[song_number]).get_length()
    pb['value'] = pygame.mixer.Sound('songs/' + songs[song_number]).get_pos()
    label['text'] =  str(songs[song_number])


def continue_song(label: Label):
    pygame.mixer.unpause()
        

def stop_song(label: Label):
    pygame.mixer.pause()


def play_next(label: Label, pb, playbut):
    playbut['text'] = '||'
    pygame.mixer.stop()
    global song_number
    try:
        song_number += 1
        stop_song(label)
        play_song(label, pb)
    except IndexError:
        song_number = 0


def play_list(label: Label, pb):
    pygame.mixer.stop()
    global song_number
    if pygame.mixer.music.get_busy():
        try:
            song_number += 1
            stop_song(label)
            play_song(label, pb)
        except IndexError:
            song_number = 0


def play_last(label: Label, pb, playbut):
    pygame.mixer.stop()
    playbut['text'] = '||'
    global song_number
    try:
        song_number -= 1
        stop_song(label)
        play_song(label, pb)
    except IndexError:
        song_number +=1
