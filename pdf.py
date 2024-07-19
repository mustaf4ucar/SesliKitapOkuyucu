import PyPDF2
from gtts import gTTS
import os
import tkinter as tk
from tkinter import filedialog



def pdf_to_text(pdf_path):
    text2 = ""
    pdf_reader = PyPDF2.PdfReader(open(pdf_path,'rb'))
    for i in range(len(pdf_reader.pages)):
        text2 += pdf_reader.pages[i].extract_text()
        return text2
    

def pdf_to_voice(text2,out):
    voice_translate = gTTS(text=text2,lang='tr') 
    voice_translate.save(out)
    

def file_push():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Dosyaları","*pdf")])
    if file_path:
        pdf_text = pdf_to_text(file_path)
        pdf_to_voice(pdf_text,"save.mp3")
        os.system("start save.mp3")


app = tk.Tk()
app.title("Sesli Kitap Uygulaması")
app.geometry("250x150")
button = tk.Button(app,text="Pdf Seç",command=file_push, padx=20,pady=20)
button.pack(pady=20)


app.mainloop()