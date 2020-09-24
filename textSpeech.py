from gtts import gTTS
import os

f = open('test.txt')
x = f.read()

audio = gTTS(text=x, lang='en', slow=False)

audio.save('test.wav')
os.system('play test.wav')