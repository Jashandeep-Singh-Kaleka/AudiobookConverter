from gtts import gTTS
import PIL.Image
import pytesseract
from tkinter import filedialog

image_to_read = filedialog.askopenfilename()
print(image_to_read)
myText = []

data = pytesseract.image_to_string(PIL.Image.open(image_to_read), lang="eng")
data = data.replace("|","I") # For some reason the image to text translation would put | instead of the letter I. So we replace | with I
data = data.split('\n')
myText.append(data)

print(myText)
