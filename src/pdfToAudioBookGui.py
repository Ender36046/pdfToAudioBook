from tkinter.filedialog import askopenfilename
import tkinter as tk
import os
import pyttsx3
from pdfreader import PDFDocument, SimplePDFViewer




def initializeTk(player):
    def initializeFile(dict):
        file = askopenfilename()
        baseFilename = os.path.basename(file)
        if os.path.splitext(file)[1] == ".pdf":
            dict["filename"] = file
            filenameLabel.config(text = f"Filename: {baseFilename}")
            getPages(file)
        else:
            filenameLabel.config(text = "Non-PDF file selected!")
            totalPagesLabel.config(text = "Total pages: n/a")

    def getPages(filename):
        fd = open(filename, "rb")
        doc = PDFDocument(fd)
        all_pages = [p for p in doc.pages()] #get all the pages of the pdf document
        totalPagesLabel.config(text = f"Total pages: {len(all_pages)}")


    def readPages(dict):
        try:
            filename = dict["filename"]
            fd = open(filename,"rb")
            doc = PDFDocument(fd)
            viewer = SimplePDFViewer(fd)
            all_pages = [p for p in doc.pages()]
            for i in range(1, len(all_pages)+1): #range is (1, page_amount +1) since viewer starts index at 1 and ends at page_amount
                viewer.navigate(i) 
                viewer.render()
                page_text = "".join(viewer.canvas.strings) # type: ignore #viewer.canvas.strings returns an array of strings of each individual character, joining them makes them one string
                player.say(page_text) #say the text of the page
                player.runAndWait() #run and wait
        except KeyError:
            pass
    
    
    filename = {}

    root = tk.Tk()
    root.title("pdfToAudioConverter")
    titleLabel = tk.Label(root, text = "pdfToAudioConverter", font= ("Arial",24))
    titleLabel.place(relx = 0.5, rely= 0.05, anchor='center')

    filenameLabel = tk.Label(root, text = f"Filename: n/a", font=("Arial", 12))
    filenameLabel.place(relx= 0.5, rely = 0.2, anchor='center')
    
    fileButton = tk.Button(root, text = "Choose file", command=lambda: initializeFile(filename),height = 2, font = ("Arial",10), width = 12)
    fileButton.place(relx = 0.15, rely =0.85, anchor='center')

    playButton = tk.Button(root, text = "Play Audio", height= 2, command= lambda: readPages(filename),font = ("Arial",10), width = 12)
    playButton.place(relx = 0.30, rely=0.85, anchor='center')

    exitButton = tk.Button(root, text = "Exit", height = 2, command = root.quit, font = ("Arial",10), width = 12)
    exitButton.place(relx = 0.45, rely = 0.85, anchor= 'center')

    totalPagesLabel = tk.Label(root, text = "Total pages: n/a", font = ("Arial", 12))
    totalPagesLabel.place(relx = 0.5, rely = 0.3, anchor="center")
    
    root.geometry("800x600")

    return root

def main():
    player = pyttsx3.init()
    root = initializeTk(player)
    root.mainloop()

if __name__ == "__main__":
    main()