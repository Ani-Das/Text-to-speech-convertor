#!/usr/bin/env python
# coding: utf-8

# In[34]:


#Python text to speech project by Aniesh Das


# In[35]:


from tkinter import *
import gtts as gTTS
import playsound
import pyttsx3


# In[36]:


root = Tk()
root.geometry("350x300") 
root.configure(bg='ghost white')
root.title("DataFlair - TEXT TO SPEECH")


# In[37]:


Label(root, text = "TEXT_TO_SPEECH", font = "arial 20 bold", bg='white smoke').pack()
Label(text ="DataFlair", font = 'arial 15 bold', bg ='white smoke' , width = '20').pack(side = 'bottom')
Msg = StringVar()
Label(root,text ="Enter Text", font = 'arial 15 bold', bg ='white smoke').place(x=20,y=60)
entry_field = Entry(root, textvariable = Msg ,width ='50')
entry_field.place(x=20,y=100)


# In[38]:


def Text_to_speech():
    txt = entry_field.get()
    #speech = gTTS(text = Message)
    #speech.save('DataFlair.mp3')
   # playsound('DataFlair.mp3')
    engine = pyttsx3.init()
    engine.say(txt)
    engine.runAndWait()


# In[39]:


def Exit():
    root.destroy()
    
def Reset():
    Msg.set("")


# In[40]:


Button(root, text = "PLAY", font = 'arial 15 bold' , command = Text_to_speech ,width = '4').place(x=25,y=140)
Button(root, font = 'arial 15 bold',text = 'EXIT', width = '4' , command = Exit, bg = 'OrangeRed1').place(x=100 , y = 140)
Button(root, font = 'arial 15 bold',text = 'RESET', width = '6' , command = Reset).place(x=175 , y = 140)

root.mainloop()


# In[ ]:




