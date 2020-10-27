# /usr/local/bin/python3 -m pip install pyttsx3
import pyttsx3
import PyPDF2
from tkinter.filedialog import *

<<<<<<< HEAD
=======

>>>>>>> ec1b5cd1c4e14c084d225439e924645ac1fbc51c
# book = open('winner-stands-alone.pdf', 'rb')
# for active selection of a book
book = askopenfilename()
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

for num in range(0, 1):
<<<<<<< HEAD
    page = pdfReader.getPage(20)
=======
    page = pdfReader.getPage(21)
>>>>>>> ec1b5cd1c4e14c084d225439e924645ac1fbc51c
    text = page.extractText()
    # text = text.lower()
    text = text.replace('\n', '')
    print(text)
    speaker = pyttsx3.init()
    speaker.say(text)
    speaker.runAndWait()


# Future imporvement
# 0. Lower case the text, and remove new lines
# 1. save last read page and line
# 2. options to skip the foreword and index
# 3. a default mp3 player for the audiobooks
# 4. capabilty to move between pages
# 5. also slow down or speed up the speed
# 6. Manually adjust the speed by replacing punc with ,,,, to slow down


# Thank you Programming hero for helping me listen to books
# coz i clearly can't read
# https://www.youtube.com/watch?v=kyZ_5cvrXJI&t=661s
