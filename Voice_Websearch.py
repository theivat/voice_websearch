#!/usr/bin/env python
# coding: utf-8

# In[24]:


import speech_recognition as sr
import webbrowser as wb


# In[25]:


sr.Microphone(device_index=1)
r=sr.Recognizer()
r.energy_threshold=5000

with sr.Microphone() as source:
    print("speak!")
    audio=r.listen(source)
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




