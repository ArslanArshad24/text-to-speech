from gtts import gTTS
import os

file = open('text1.txt')
file_read =file.read()

language= 'en'
audio = gTTS(text=file_read,lang=language,slow=False)

##################   wav Audio
audio.save('audio1.wav')
os.system('audio1.wav')

#####################   mp3 Audio
audio.save('audio2.mp3')
os.system('audio2.mp3')