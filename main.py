import audio
import prompt

print(prompt.c)
print(prompt.count)

audio.text = prompt.c
audio.tts = audio.gTTS(audio.text,lang='es', slow=False, pre_processor_funcs = [audio.abbreviations, audio.end_of_line]) 
audio.tts.save('traudio.mp3')
audio.mixer.init()
audio.mixer.music.load("traudio.mp3")
audio.mixer.music.play()
audio.time.sleep(prompt.count)