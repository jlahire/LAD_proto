import tkinter as tk
import PIL
import PIL.ImageTk as ImageTk
import PIL.Image as Image
from gtts import gTTS
from pygame import mixer
import time
import words

count = 2

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

mixer.init()

def select_category(category):
    category_var.set(category)  # Set the category variable
    sub_cats = list(ls_words[category].keys())
    sub_cat_var.set(sub_cats[0])
    global sub_cat_menu
    if sub_cat_menu:
        sub_cat_menu.destroy()
    create_sub_category_menu(sub_cats)
    # select_sub_category(sub_cats[0])

def select_sub_category(sub_cat):
    category = category_var.get()
    print(f"Category: {category}")
    print(f"Sub Category: {sub_cat}")
    if category:
        value = ls_words[category].get(sub_cat)
        print(f"Value: {value}")
        if value == "ten":
            mixer.music.load("tenaudio.mp3")
            mixer.music.play()
        elif value == "tes":
            mixer.music.load("tesaudio.mp3")
            mixer.music.play()
    else:
        print("No category selected")
    # Rest of the code...

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
