from tkinter import *
from gtts import gTTS
from playsound import playsound
from PIL import Image,ImageTk

root = Tk()
root.geometry('1200x1000+0+0')

root.title('TEXT TO VOICE')

#root.bg=ImageTk.PhotoImage(file="/users/ajaysihag/Downloads/bs.jpeg")
#bg=Label(root,image=root.bg).place(x=0,y=0,relheight=1,relwidth=1)

#Heading

Label(root, text = 'TEXT TO VOICE' , font='arial 60 bold',fg='blue',bg='lightblue' ).pack()

#label

Label(root, text ='Enter Text', font ='arial 55 bold',fg='green',bg='lightblue').place(x=450,y=230)

#text variable

Msg = StringVar()

#Entry field for the text message

entry_field = Entry(root,textvariable =Msg,font='arial 40 bold', width ='40',fg='black',bg='lightblue')
entry_field.place(x=125,y=330)

# Three Functions to Speak Exit and Reset

def Speak():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('ritik.mp3')
    playsound('ritik.mp3')

def Exit():
    root.destroy()

def Reset():
    Msg.set("")

#Button for above three functions

Button(root, text = "PLAY" , font = 'arial 40 bold', command = Speak, width =4).place(x=280, y=410)
Button(root,text = 'EXIT',font = 'arial 40 bold' , command = Exit, bg = 'blue').place(x=510,y=410)
Button(root, text = 'RESET', font='arial 40 bold', command = Reset).place(x=710 , y =410)


#infinite loop to run program
root.mainloop()
