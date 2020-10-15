from gtts import gTTS
import pygame
import os
import tkinter as tkr
import fitz
from PIL import Image
import pytesseract
from tkinter.filedialog import *


# create a directory, for the images
current_directory = os.getcwd()
final_directory = os.path.join(current_directory,r'Text_to_speech_software')
if not os.path.exists(final_directory):
    os.makedirs(final_directory)
print(current_directory)
print(final_directory)

# pickpdf to read via tkinter
book = askopenfilename()

# open the pdf to be read
doc = fitz.open(book)

# Open page, it is zero indexed
page = doc.loadPage(20)
zoom_x = 2.0
zoom_y = 2.0
mat = fitz.Matrix(zoom_x, zoom_y)
pix = page.getPixmap(matrix=mat)
output = os.path.join(final_directory, r"image_to_read.png")
pix.writePNG(output)
