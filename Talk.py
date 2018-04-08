# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 16:17:04 2018

@author: Darshan
"""
from gtts import gTTS
import os

def Talk(mytext):
    tts = gTTS(text= mytext, lang='en')
    tts.save("sound.mp3")
    os.system("mpg321 sound.mp3")
    return