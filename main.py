from tkinter import *
from gtts import gTTS
import playsound
import PyPDF2
from tkinter.filedialog import askopenfilename

def text_to_speech():
    text = text_box.get("1.0", "end-1c")
    speech = gTTS(text)
    speech.save('DataFlair.mp3')
    play()

def play():
    playsound.playsound(r'C:\Users\roseb\audiobook\DataFlair.mp3')

def play_from_file():
    playsound.playsound(r'C:\Users\roseb\audiobook\audio.mp3')
#ui

def pdf_to_txt():
    with open('text_file.txt', 'w') as f:
        f.truncate()

    with open(f"{open_file()}", 'rb') as pdf:
        pdf_reader = PyPDF2.PdfReader(pdf)
        x = len(pdf_reader.pages)
        for i in range(x):
            page_obj = pdf_reader.pages[i]
            text = page_obj.extract_text()


            with open('text_file.txt', 'a') as file:
                file.writelines(text)
    with open('text_file.txt', 'r') as fil:
        t = gTTS(fil.read())
    t.save('audio.mp3')

def open_file():
    file_path = askopenfilename()
    if file_path is not None:
        pass
    print(file_path)
    return file_path


window = Tk()
window.config(background='#8294C4')
window.minsize(800, 600)

lab = Label(text='Text to Audio', font=("Stencil Std", "20", "bold"), background='#8294C4', fg='#F5EFE7')
lab.place(x=300, y=20)

lab = Label(text='Enter text here:', font=("Stencil Std", "12", "bold"), background='#8294C4', fg='#F5EFE7')
lab.place(x=80, y=70)

text_box = Text(window, background='#F5EFE7')
text_box.place(x=80, y=100)



photo = PhotoImage(file="play.png")
but = Button(window, command=lambda :text_to_speech(), image=photo, highlightthickness=0, border=0, borderwidth=0)
but.place(x=600, y=440)


file = PhotoImage(file="upload.png")
upload = Button(window, text="Upload file", image=file, command=lambda :pdf_to_txt(), background='#8294C4', borderwidth=0, pady=0, padx=0)
upload.place(x=220, y=500)


play_from = PhotoImage(file="fromfile.png")
play_file = Button(window, text="Play from file", image=play_from, command=lambda :play_from_file(), background='#8294C4', borderwidth=0)
play_file.place(x=440, y=500)


window.mainloop()



