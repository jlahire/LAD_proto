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
window.title("Language Assistance Device -- Prototype")
window.attributes("-fullscreen", True)  # Make the window fullscreen

# Color schemes
color_schemes = {
    "Rainbow Delight": {
        "primary": "IndianRed",
        "secondary": "DarkOrange",
        "accent": "Gold",
    },
    "Nature's Harmony": {
        "primary": "MediumSeaGreen",
        "secondary": "Burlywood",
        "accent": "PeachPuff",
    },
    "Dreamy Pastels": {
        "primary": "PowderBlue",
        "secondary": "LavenderBlush",
        "accent": "LightPink",
    },
}

current_color_scheme = "Nature's Harmony"

ls_words = {
    "greeting": gre,
    "food": foo,
    "animal": ani,
    "color": col,
    "action": act,
    "object": obj,
    "drink": dri,
    "feeling": fee,
}

sub_cat_menu = None
category_var = tk.StringVar()

mixer.init()

# Function to move the settings button to the top right corner
def move_settings_button_bottom_right():
    settings_button.place(x=window.winfo_screenwidth()-110, y=window.winfo_screenheight()-60)


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
        sub_cat_menu = None  # Reset sub_cat_menu variable
    result_label["text"] = ""
    reset_button.pack_forget()

    # Reposition reset button
    reset_button.pack(side="bottom", pady=10)


def create_category_tabs():
    category_frame = tk.Frame(window, bg=color_schemes[current_color_scheme]["primary"])
    category_frame.pack(fill="x")

    for category in ls_words.keys():
        category_button = tk.Button(
            category_frame,
            text=category.capitalize(),
            width=15,
            fg=color_schemes[current_color_scheme]["primary"],
            bg=color_schemes[current_color_scheme]["secondary"],
            activebackground=color_schemes[current_color_scheme]["accent"],
            activeforeground=color_schemes[current_color_scheme]["primary"],
            relief="flat",
            command=lambda category=category: select_category(category),
        )
        category_button.pack(side="left", padx=10, pady=5)

def create_sub_category_menu(sub_cats):
    global sub_cat_menu
    sub_cat_menu_frame = tk.Frame(window, bg=color_schemes[current_color_scheme]["primary"])
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
            bg=color_schemes[current_color_scheme]["secondary"],
            activebackground=color_schemes[current_color_scheme]["accent"],
            relief="flat",
        )
        sub_cat_button.image = photo

        row = i % rows
        column = i // rows
        sub_cat_button.grid(row=row, column=column, padx=10, pady=5)

    # Adjust the frame size based on the number of buttons
    sub_cat_menu_frame.grid_columnconfigure(0, weight=1)
    sub_cat_menu_frame.grid_columnconfigure(columns, weight=1)

def change_color_scheme(new_scheme):
    global current_color_scheme
    current_color_scheme = new_scheme

    # Update window background color
    window.configure(bg=color_schemes[current_color_scheme]["primary"])

    # Update category button colors
    for widget in category_frame.winfo_children():
        widget.configure(
            fg=color_schemes[current_color_scheme]["primary"],
            bg=color_schemes[current_color_scheme]["secondary"],
            activebackground=color_schemes[current_color_scheme]["accent"],
            activeforeground=color_schemes[current_color_scheme]["primary"],
        )

    # Check if sub_cat_menu exists
    if sub_cat_menu is not None:
        # Update sub-category button colors
        for widget in sub_cat_menu.winfo_children():
            widget.configure(
                bg=color_schemes[current_color_scheme]["secondary"],
                activebackground=color_schemes[current_color_scheme]["accent"],
            )

    # Update result label color
    result_label.configure(bg=color_schemes[current_color_scheme]["primary"])

    # Update reset button colors
    reset_button.configure(
        fg=color_schemes[current_color_scheme]["primary"],
        bg=color_schemes[current_color_scheme]["secondary"],
        activebackground=color_schemes[current_color_scheme]["accent"],
    )

    # Update settings button colors
    settings_button.configure(
        fg=color_schemes[current_color_scheme]["primary"],
        bg=color_schemes[current_color_scheme]["secondary"],
        activebackground=color_schemes[current_color_scheme]["accent"],
    )

    # Move the settings button to the top right corner
    move_settings_button_bottom_right()

# Settings button callback
def open_settings():
    settings_window = tk.Toplevel(window)
    settings_window.title("Settings")
    settings_window.geometry("400x300")

    settings_label = tk.Label(settings_window, text="Select Color Scheme:")
    settings_label.pack(pady=10)

    # Color scheme radio buttons
    for scheme in color_schemes.keys():
        color_scheme_radio = tk.Radiobutton(
            settings_window,
            text=scheme,
            value=scheme,
            variable=color_scheme_var,
            command=lambda: change_color_scheme(color_scheme_var.get()),
        )
        color_scheme_radio.pack(pady=5)
    move_settings_button_bottom_right()

# Initialize color scheme variable
color_scheme_var = tk.StringVar(window)
color_scheme_var.set(current_color_scheme)

# Category label and tabs
category_label = tk.Label(window, text="Choose a category:")
category_label.pack()
category_frame = tk.Frame(window)
category_frame.pack(fill="x")
create_category_tabs()

sub_cat_var = tk.StringVar(window)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

reset_button = tk.Button(window, text="Reset", command=reset_selection)
reset_button.pack(side="bottom", pady=10)

# Settings button
settings_button = tk.Button(window, text="Settings", command=open_settings)
settings_button.pack(side="top", padx=10, pady=5)

# Apply color scheme
change_color_scheme(current_color_scheme)

window.mainloop()
