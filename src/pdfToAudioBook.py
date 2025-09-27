import pyttsx3
import pdfreader
from pdfreader import PDFDocument, SimplePDFViewer
from tkinter.filedialog import *

file = askopenfilename()
fd = open(file, "rb")
doc = PDFDocument(fd)
viewer = SimplePDFViewer(fd)
player = pyttsx3.init()

all_pages = [p for p in doc.pages()]

for i in range(1, len(all_pages)+1):
    viewer.navigate(i)
    viewer.render()
    page_text = "".join(viewer.canvas.strings)
    player.say(page_text)
    player.runAndWait()