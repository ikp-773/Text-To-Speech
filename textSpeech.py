from gtts import gTTS
from playsound import playsound
import os

f = open('test.txt')
x = f.read()

audio = gTTS(text=x, lang='en', slow=False)
audioFile = 'test2.wav'

audio.save(audioFile)
playsound(audioFile)
