import PyPDF2
import pyttsx3
from tkinter import *
from tkinter import filedialog


def play():
    file=filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("PDF Files", "*.pdf"), ("all files", "*.*") ))
    label_file_explorer.configure(text="File Opened: "+ file)
    pdf=PyPDF2.PdfFileReader(file)
    from_page=pdf.getPage(24)    
    t=from_page.extractText()
    s=pyttsx3.init()
    n=145
    s.setProperty('rate',n)
    s.say(t)
    s.runAndWait()

    


window = Tk()
window.title('File Explorer')
window.geometry("500x500")

window.configure(background = "white")
label_file_explorer = Label(window, text = "File Explorer using Tkinter", width = 100, height = 4, fg = "blue")

button_exit = Button(window, text = "Exit", command = exit)
button_Play = Button(window, text = "Play", command = play)


label_file_explorer.grid(column = 1,row = 1)

button_exit.grid(column = 1,row = 3)
button_Play.grid(column = 1,row = 4)

window.mainloop()
