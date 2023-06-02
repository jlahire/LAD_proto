from gtts import gTTS
from gtts.tokenizer.pre_processors import abbreviations, end_of_line
from pygame import mixer
import time
import prompt

text = prompt.a
tts = gTTS(text,
           lang='en',
           slow=False,
           pre_processor_funcs=[abbreviations, end_of_line])
tts.save('tenaudio.py.mp3')
mixer.init()
mixer.music.load("tenaudio.py.mp3")
mixer.music.play()
time.sleep(prompt.count)

text = prompt.b
tts = gTTS(text,
           lang='es',
           slow=False,
           pre_processor_funcs=[abbreviations, end_of_line])
tts.save('tesaudio.py.mp3')
mixer.init()
mixer.music.load("tesaudio.py.mp3")
mixer.music.play()
time.sleep(prompt.count)
