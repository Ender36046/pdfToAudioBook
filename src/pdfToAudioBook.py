import pyttsx3
from pdfreader import PDFDocument, SimplePDFViewer
from tkinter.filedialog import *

def main():
    file = askopenfilename() #open the pdf file on your computer
    fd = open(file, "rb")
    doc = PDFDocument(fd)
    viewer = SimplePDFViewer(fd)
    player = pyttsx3.init()

    all_pages = [p for p in doc.pages()] #get all the pages of the pdf document

    for i in range(1, len(all_pages)+1): #range is (1, page_amount +1) since viewer starts index at 1 and ends at page_amount
        viewer.navigate(i) 
        viewer.render()
        page_text = "".join(viewer.canvas.strings) #viewer.canvas.strings returns an array of strings of each individual character, joining them makes them one string
        player.say(page_text) #say the text of the page
        player.runAndWait() #run and wait

if __name__ == "__main__":
    main()