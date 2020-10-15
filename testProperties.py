# Testing out various properties of the text to speech
# So that one can provide the options to the user
import pyttsx3

engine = pyttsx3.init('nsss')

engine.say("This is a voice test. This , is ,, a ,,, pace ,,,, test")
engine.runAndWait()

# The properties include:
# rate
# voice
# volume
# voices
print(engine.getProperty('rate'))
print(engine.getProperty('voice'))
print(engine.getProperty('volume'))
voices = engine.getProperty('voices')

# Each voice further has:
# age
# gender
# id
# languages
# name
for voice in voices:
    print("Voice: %s" % voice.name)
    print(" - ID: %s" % voice.id)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)
    print("\n")
# The english voices are:
# Alex - en_US - USA - Male - [0]
# Daniel - en_GB - Britain - Male - [7]
# Fiona - en_scotland - Female - [10]
# Fred - en_US - USA - Male - [11]
# Karen - en_AU - Australia - Female - [17]
# Moira - en_IE - Eire - Female - [28]
# Rishi - en_IN - India - Male - [32]
# Samantha - en_US - USA - Female - [33]
# Tessa - en_ZA - South Africe - Female - [37]
# Veena - en_IN - Female - [40]
# Victoria - en_US - Female - [41]

# The above references are for my system, that is running Unix/OSx
# For every system the player will do a scan and provide a list of
# available voices, initital just the english ones

engine.setProperty('voice', voices[11].id)
engine.setProperty('rate', 150)

engine.say(' This is a voice and rate test')
engine.runAndWait()
