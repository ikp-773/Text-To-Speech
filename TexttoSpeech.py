from gtts import gTTS
import os

f = open("test.txt", "r").read()

audio = gTTS(text = str(f), lang = "en", slow = False)

audio.save("test.mp3")
os.system("test.mp3")
