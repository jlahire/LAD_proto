import words

gre = words.greeting
foo = words.food
ani = words.animal
col = words.color
act = words.action
obj = words.object
dri = words.drink
fee = words.feeling

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

# tr_words = {}

# need to add count modifier and explore creating a syllable library to determine how long the pause should be in the audio
count = 0


prompt = input('\nWould you like to start? (y/n)\n >> ')
for a in prompt:
  a = a.lower()
  if a == 'n':
    print('\nClosing...')
    exit()
  else:
    continue

category = input(
  '\nChoose a category: \n Greeting \n Food \n Animal \n Color \n Action \n Object \n Drink \n Feeling \n >> '
)

for c in category.split():
  c = c.lower()
  if c in ls_words:
    words_dict = ls_words[c]
    sub_cat_prompt = f"\nChoose a {c.capitalize()}:\n"
    sub_cat_prompt += "\n".join(f"{index + 1}. {key.capitalize()}"
                                for index, key in enumerate(words_dict.keys()))
    sub_cat_prompt += "\n>> "
    sub_cat_index = int(input(sub_cat_prompt)) - 1
    sub_cats = list(words_dict.keys())
    selected_sub_cat = sub_cats[sub_cat_index]
    a = selected_sub_cat.lower()
    b = words_dict[selected_sub_cat]

    print(a, b)
