import pyttsx3
import PyPDF2
from tkinter import *
from gtts import gTTS
import os
import tkinter as tkr
import fitz
from PIL import Image
import pytesseract
import PIL.Image
import time
from tkinter.filedialog import askopenfilename


def openbook():
    global book
    # book = open('winner-stands-alone.pdf', 'rb')
    # for active selection of a book
    book = askopenfilename() #'/Users/apple/Desktop/2020/iCantRead/sampleBook.pdf' 
    root.destroy()


book = "unassigned"
root = Tk()
root.wm_withdraw()
openbook()
root.mainloop()


# Button(root, text='File Open', command=openBook).pack(fill=X)

pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

# create a directory, for the images
current_directory = os.getcwd()
final_directory = os.path.join(current_directory, r'Text_Images')
if not os.path.exists(final_directory):
    os.makedirs(final_directory)
print(current_directory)
print(final_directory)

# open the pdf to be read
doc = fitz.open(book)

# current page variable
currentPage = 19

# Open page, it is zero indexed
page = doc.loadPage(currentPage)
zoom_x = 2.0
zoom_y = 2.0
mat = fitz.Matrix(zoom_x, zoom_y)
pix = page.getPixmap(matrix=mat)
output = os.path.join(final_directory, r"image"+str(currentPage)+".png")
pix.writePNG(output)

image_to_read = (str(final_directory)+"/image"+str(currentPage)+".png")
print(image_to_read)
myText = []

# This data extraction needs to be 
# The cleanup stage
data = pytesseract.image_to_string(PIL.Image.open(image_to_read), lang="eng")
data = data.replace("|", "I")  # For some reason the image to text translation would put | instead of the letter I. So we replace | with I
data = data.split('\n')
myText.extend(data)

# myText = ['The name of some colors are', 'red', 'green', 'blue', 'yellow']
# Then loop for elements
print(myText)


def cb(name):
    print(name, end=' ', flush=True)


# def onEnd(name):
#    speaker.endLoop()


# Per line recitation
speaker = pyttsx3.init()
speaker.connect('started-utterance', cb)
# speaker.startLoop(False)
for line in myText:
    if line != '' and line != '\x0c':
        # print(line)
        speaker.say(line, name=line)
        # speaker.iterate()
speaker.runAndWait()
del speaker
print("Done speaking")


# speaker.connect('finished-utterence', onEnd)



# speaker.startLoop()
# speaker.endLoop()



# for num in range(0, 1):
#     page = pdfReader.getPage(21)
#     text = page.extractText()
#     # text = text.lower()
#     text = text.replace('\n', '')
#     print(text)
#     speaker = pyttsx3.init()
#     speaker.say(text)
#     speaker.runAndWait()
