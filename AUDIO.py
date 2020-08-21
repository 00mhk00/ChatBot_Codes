import os
from gtts import gTTS
text ="Welcome to Mehak aroraaaa's text to speech converter"

# language in which you want to convert
lang='en'

myobj = gTTS(text=text,lang=lang,slow=False)
myobj.save("audio.mp3")

#playing the converted file
os.system("audio.mp3")