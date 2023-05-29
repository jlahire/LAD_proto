from gtts import gTTS
from gtts.tokenizer.pre_processors import abbreviations, end_of_line
from pygame import mixer
import time
import prompt

print(prompt.e)

text = prompt.e
tts = gTTS(text,lang='en', slow=False, pre_processor_funcs = [abbreviations, end_of_line]) 
tts.save('traudio.mp3')
mixer.init()
mixer.music.load("traudio.mp3")
mixer.music.play()
time.sleep(prompt.count)