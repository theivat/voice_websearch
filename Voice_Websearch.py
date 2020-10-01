#!/usr/bin/env python
# coding: utf-8

# In[24]:

#voice recognition module
import speech_recognition as sr

#To open link/search engine
import webbrowser as wb


# In[25]:

#basic initialisation
sr.Microphone(device_index=1)
r=sr.Recognizer()
r.energy_threshold=5000

#taking input from microphone
with sr.Microphone() as source:
    print("speak!")
    audio=r.listen(source)
    
#main logic
    try:
        text=r.recognize_google(audio)
        print("you said :{}".format(text))
        url='https://www.google.com/search?q='
        search_url=url+text
        wb.open(search_url)
    except:
        print("i don't understand what you say")


# In[ ]:





# In[ ]:




