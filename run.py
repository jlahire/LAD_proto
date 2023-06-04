import tkinter as tk
import PIL
import PIL.ImageTk as ImageTk
import PIL.Image as Image
from gtts import gTTS
from gtts.tokenizer.pre_processors import abbreviations, end_of_line
from pygame import mixer
import time
import prompt
import words

gre = words.greeting
foo = words.food
ani = words.animal
col = words.color
act = words.action
obj = words.object
dri = words.drink
fee = words.feeling

window = tk.Tk()
window.title("Language Assistance Device -- Protoype")

ls_words = {
  "greeting": gre,
  "food": foo,
  "animal": ani,
  "color": col,
  "action": act,
  "object": obj,
  "drink": dri,
  "feeling": fee
}

sub_cat_menu = None
category_var = tk.StringVar()


def select_category(category):
  sub_cats = list(ls_words[category].keys())
  sub_cat_var.set(sub_cats[0])
  global sub_cat_menu
  if sub_cat_menu:
    sub_cat_menu.destroy()
  create_sub_category_menu(sub_cats)
  select_sub_category(sub_cats[0])


def select_sub_category(sub_cat):
  category = category_var.get()
  a = sub_cat.lower()
  b = ls_words[category][sub_cat]
  result_label["text"] = f"{a}: {b}"
  reset_button.pack()

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


def reset_selection():
  category_var.set("")
  sub_cat_var.set("")
  global sub_cat_menu
  if sub_cat_menu:
    sub_cat_menu.destroy()
  result_label["text"] = ""
  reset_button.pack_forget()


def create_sub_category_menu(sub_cats):
  global sub_cat_menu
  sub_cat_menu_frame = tk.Frame(window)
  sub_cat_menu_frame.pack()
  for sub_cat in sub_cats:
    image_path = f"images/{sub_cat.lower()}.png"
    image = Image.open(image_path).resize((100, 100))
    photo = ImageTk.PhotoImage(image)
    sub_cat_button = tk.Button(
      sub_cat_menu_frame,
      image=photo,
      command=lambda sub_cat=sub_cat: select_sub_category(sub_cat))
    sub_cat_button.image = photo
    sub_cat_button.pack(side="left")


category_label = tk.Label(window, text="Choose a category:")
category_label.pack()
for category in ls_words.keys():
  category_button = tk.Button(
    window,
    text=category.capitalize(),
    width=15,
    command=lambda category=category: select_category(category))
  category_button.pack()

sub_cat_var = tk.StringVar(window)

result_label = tk.Label(window, text="")
result_label.pack()

reset_button = tk.Button(window, text="Reset", command=reset_selection)

window.mainloop()
