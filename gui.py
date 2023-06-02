import tkinter as tk
import PIL
import PIL.ImageTk as ImageTk
import PIL.Image as Image

import words

gre = words.greeting
foo = words.food
ani = words.animal
col = words.color
act = words.action
obj = words.object
dri = words.drink
fee = words.feeling

# Create a Tkinter window
window = tk.Tk()
window.title("Purple Irish Penguins Grab Sea Wookie Star Mittens")

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


# Function to handle category selection
def select_category(category):
  sub_cats = list(ls_words[category].keys())
  sub_cat_var.set(sub_cats[0])  # Set the default value for sub-category
  sub_cat_menu.destroy()  # Clear the existing options
  create_sub_category_menu(sub_cats)
  select_sub_category(sub_cats[0])  # Select the default sub-category


# Function to handle sub-category selection
def select_sub_category(sub_cat):
  category = category_var.get()
  a = sub_cat.lower()
  b = ls_words[category][sub_cat]
  result_label["text"] = f"{a}: {b}"
  reset_button.pack()  # Show the reset button


# Function to reset the selection
def reset_selection():
  category_var.set("")  # Clear the selected category
  sub_cat_var.set("")  # Clear the selected sub-category
  sub_cat_menu.destroy()  # Clear the sub-category menu
  result_label["text"] = ""  # Clear the result label
  reset_button.pack_forget()  # Hide the reset button


# Function to create sub-category menu buttons
def create_sub_category_menu(sub_cats):
  sub_cat_menu_frame = tk.Frame(window)
  sub_cat_menu_frame.pack()
  for sub_cat in sub_cats:
    image_path = f"images/{sub_cat.lower()}.png"  # Assuming the images are stored in a folder named "images"
    image = Image.open(image_path).resize(
      (100, 100))  # Resize the image to fit the button
    photo = ImageTk.PhotoImage(image)
    sub_cat_button = tk.Button(
      sub_cat_menu_frame,
      image=photo,
      command=lambda sub_cat=sub_cat: select_sub_category(sub_cat))
    sub_cat_button.image = photo  # Save a reference to the image to prevent it from being garbage collected
    sub_cat_button.pack(side="left")


# Create the category selection buttons
category_label = tk.Label(window, text="Choose a category:")
category_label.pack()
for category in ls_words.keys():
  category_button = tk.Button(
    window,
    text=category.capitalize(),
    width=15,
    command=lambda category=category: select_category(category))
  category_button.pack()

# Create the sub-category selection buttons
sub_cat_var = tk.StringVar(window)

# Create the result label
result_label = tk.Label(window, text="")
result_label.pack()

# Create the reset button
reset_button = tk.Button(window, text="Reset", command=reset_selection)

# Start the Tkinter event loop
window.mainloop()
