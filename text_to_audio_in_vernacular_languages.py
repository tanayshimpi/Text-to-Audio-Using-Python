#Language in which you want to convert
language = 'hi'
from gtts import gTTS
file= open('demo.txt','r').read().replace('\n',' ')
import os
text = file
language = 'hi'
speech = gTTS(text=str(file), lang=language , slow=False)
speech = gTTS(text=text, lang=language , slow=False)

speech.save("final.mp3")
#on Program
