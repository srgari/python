#%%
### Hangman!
import subprocess
import requests 
import re 
import random
import time 
#%%
r = requests.get('https://www.worldometers.info/geography/alphabetical-list-of-countries/')
countries = re.findall('15px">(.{1,20})?</td', r.text)

def draw_person(attempt = 0, hidden_word = '', real_word = '', wrong_ones = ''):
    draw = """ attempt {attempt}
{wrong_ones}
________   
{g}     {a}     
|    {b}{c}{d} 
|   _{e}_{f}_      
|___{h}_  
{hidden_word}
{real_word}"""



    a = 'O'                if attempt > 0 and attempt <= 6 else  'O - I\'m dead!' if attempt >=7  else  ' ' 
    c = '|'                if attempt > 1 else ' ' 
    b = '/'                if attempt > 2 else ' '      
    d = '\\'               if attempt > 3 else ' '  
    e = '/'                if attempt > 4 else ' '  
    f = '\\'               if attempt > 5 else ' '  
    g = '|     |\n|'       if attempt > 6 else '|'  
    h = ' '                if attempt > 6 else 'XXXXX'  

    subprocess.run('clear')
    print('\r',
        draw.format(
            a = a,
            b = b,
            c = c,
            d = d,
            e = e,
            f = f,
            g = g,
            h = h,
            attempt = attempt,
            hidden_word = hidden_word,
            real_word = real_word,
            wrong_ones = wrong_ones
            ), end = '\n'
    )

def guess_word():
    word = random.choice(countries)
    hidden_word = list(' '*len(word))
    wrong_words = []
    n = 0
    while ' ' in hidden_word:
        draw_person(n, ''.join(hidden_word), '', ''.join(wrong_words))
        attempt = input('guess letter\n')
        print(f'you pressed {attempt}')      
        
        if attempt in word:
            hidden_word.remove(' ')
            hidden_word.insert(word.index(attempt), attempt)
            print(word, ''.join(hidden_word))
        else:
            wrong_words.append(attempt) 
            n+=1

        if n == 7:
            draw_person(n, ''.join(hidden_word), word)
            print('Game over!')
            break
            

guess_word()
