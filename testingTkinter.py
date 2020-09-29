import tkinter as tkr
import pyttsx3

engine = pyttsx3.init('nsss')

# Window initialization
player = tkr.Tk(screenName='The Machine can read it to me')

# window dimensions
player.geometry("350x350")

# defining actions


def play():
    engine.say("Checking the play function, Checking the play function, Checking the play function, Checking the play function, Checking the play function")
    engine.startLoop()


def stop():
    engine.endLoop()


# creating the buttons
Button1 = tkr.Button(player, width=5, height=3, text="PLAY", command=play)
Button1.pack(fill='x')

Button2 = tkr.Button(player, width=5, height=3, text="STOP", command=stop)
Button2.pack(fill='x')


# Activating the applicatio
player.mainloop()
