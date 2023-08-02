from tkinter import *
import speech_recognition as sr
root = Tk()
root.geometry("800x400")
root.title("hello")

def audio():
    speech_recognisor = sr.Recognizer()
    with sr.Microphone() as source:
        audio = speech_recognisor.listen(source)
        voice_d = ''
        try:
            voice_d = speech_recognisor.recognize_google(audio, language="es-mx")
        except sr.UnknownValueError:
            print("hubo un fallo")

    print(voice_d)

btn = Button(root, text="graba", command=audio)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()