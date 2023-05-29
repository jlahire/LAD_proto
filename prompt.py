words = {}
count = 0



prompt = input('\nWould you like to start? (y/n)\n >> ')
for a in prompt:
    a == a.lower()
    if a == 'n':
        print('\nClosing...')
        exit()
    else:
        continue
    
category = input('\nChoose a category: \n Hello \n Food \n Feeling \n >> ')
for c in category.split():
    if category == 'hello':
        e = 'hello'
        c = 'hola'
        words[e] = words.get(e,0) + 1
        words[c] = words.get(c,0) + 1        
        
    elif category == 'food':
        e = 'food'
        c = 'alimento'
        words[e] = words.get(e,0) + 1
        words[c] = words.get(c,0) + 1  
        
    elif category == 'feeling':
        e = 'feeling'
        c = 'sentimiento'
        words[e] = words.get(e,0) + 1
        words[c] = words.get(c,0) + 1  
    else:
        e = 'incorrect input'
        c = 'entrada incorrecta'
        words[e] = words.get(e,0) + 1
        words[c] = words.get(c,0) + 1  

for k,v in words.items():
    count = count + int(v)
