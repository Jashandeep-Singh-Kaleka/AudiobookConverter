import tkinter as tkr
import pygame
from gtts import gTTS


# engine = pyttsx3.init('nsss')
# Getting a dummy file to test out the player
def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    return filename


# Window initialization
player = tkr.Tk(screenName='The Machine can read it to me')

# window dimensions
player.title("Audio Player")
player.geometry("350x350")


# defining actions
def play():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(speak("This is a player test"))
    pygame.mixer.music.play()


def stop():
    pygame.mixer.music.stop()


# creating the buttons
Button1 = tkr.Button(player, width=5, height=3, text="PLAY", command=play)
Button1.pack(fill='x')

Button2 = tkr.Button(player, width=5, height=3, text="STOP", command=stop)
Button2.pack(fill='x')

# Page Number, Song Name for now
label1 = tkr.LabelFrame(player, text="Page Number")


# Activating the application
player.mainloop()
