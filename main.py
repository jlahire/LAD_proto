import tkinter as tk
import PIL
import PIL.ImageTk as ImageTk
import PIL.Image as Image
from gtts import gTTS
from gtts.tokenizer.pre_processors import abbreviations, end_of_line
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
window.configure(bg="light blue")
window.geometry("800x600")

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
    category_var.set(category)
    sub_cats = list(ls_words[category].keys())
    sub_cat_var.set(sub_cats[0])
    global sub_cat_menu
    if sub_cat_menu:
        sub_cat_menu.destroy()
    create_sub_category_menu(sub_cats)

def select_sub_category(sub_cat):
    category = category_var.get()
    print(f"Category: {category}")
    print(f"Sub Category: {sub_cat}")
    if category:
        value = ls_words[category].get(sub_cat)
        print(f"Value: {value}")
        text = sub_cat
        tts = gTTS(text, lang='en', slow=False, pre_processor_funcs=[abbreviations, end_of_line])
        tts.save('tenaudio.py.mp3')
        mixer.music.load("tenaudio.py.mp3")
        mixer.music.play()
        time.sleep(count)

        text = value
        tts = gTTS(text, lang='es', slow=False, pre_processor_funcs=[abbreviations, end_of_line])
        tts.save('tesaudio.py.mp3')
        mixer.music.load("tesaudio.py.mp3")
        mixer.music.play()
        time.sleep(count)
    else:
        print("No category selected")

def reset_selection():
    category_var.set("")
    sub_cat_var.set("")
    global sub_cat_menu
    if sub_cat_menu:
        sub_cat_menu.destroy()
    result_label["text"] = ""
    reset_button.pack_forget()

    # Reposition reset button
    reset_button.pack(side="bottom", pady=10)

def create_category_tabs():
    category_frame = tk.Frame(window, bg="dark blue")
    category_frame.pack(fill="x")

    for category in ls_words.keys():
        category_button = tk.Button(
            category_frame,
            text=category.capitalize(),
            width=15,
            fg="white",
            bg="dark blue",
            activebackground="light blue",
            activeforeground="white",
            relief="flat",
            command=lambda category=category: select_category(category)
        )
        category_button.pack(side="left", padx=10, pady=5)

def create_sub_category_menu(sub_cats):
    global sub_cat_menu
    sub_cat_menu_frame = tk.Frame(window, bg="light blue")
    sub_cat_menu_frame.pack(pady=10)

    rows = 2
    columns = len(sub_cats) // rows + 1

    for i, sub_cat in enumerate(sub_cats):
        image_path = f"images/{sub_cat.lower()}.png"
        image = Image.open(image_path).resize((100, 100))
        photo = ImageTk.PhotoImage(image)

        sub_cat_button = tk.Button(
            sub_cat_menu_frame,
            image=photo,
            command=lambda sub_cat=sub_cat: select_sub_category(sub_cat),
            bg="light blue",
            activebackground="light blue",
            relief="flat"
        )
        sub_cat_button.image = photo

        row = i % rows
        column = i // rows
        sub_cat_button.grid(row=row, column=column, padx=10, pady=5)

    # Adjust the frame size based on the number of buttons
    sub_cat_menu_frame.grid_columnconfigure(0, weight=1)
    sub_cat_menu_frame.grid_columnconfigure(columns, weight=1)

category_label = tk.Label(window, text="Choose a category:", bg="light blue")
category_label.pack()
create_category_tabs()

sub_cat_var = tk.StringVar(window)

result_label = tk.Label(window, text="", bg="light blue")
result_label.pack(pady=10)

reset_button = tk.Button(window, text="Reset", command=reset_selection)

window.mainloop()
