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
countries = [x for x in countries if ' ' not in x]

def draw_person(attempt = 0, hidden_word = '', real_word = '', wrong_ones = ''):
    
    a = 'O'                if attempt > 0 and attempt <= 6 else  'O - I\'m dead!' if attempt >=7  else  ' ' 
    c = '|'                if attempt > 1 else ' ' 
    b = '/'                if attempt > 2 else ' '      
    d = '\\'               if attempt > 3 else ' '  
    e = '/'                if attempt > 4 else ' '  
    f = '\\'               if attempt > 5 else ' '  
    g = '|     |\n|'       if attempt > 6 else '|'  
    h = ' '                if attempt > 6 else 'XXXXX'  

    draw = f""" attempt {attempt}
{wrong_ones}
________   
{g}     {a}     
|    {b}{c}{d} 
|   _{e}_{f}_      
|___{h}_  
{hidden_word}
{real_word}"""



    subprocess.run('clear')
    print(draw)

def guess_word():
    word = random.choice(countries)
    # word = 'Madagascar'
    sel = list(word)
    hidden_word = list(' '*len(word))
    wrong_words = []
    n = 0
    while ' ' in hidden_word:
        draw_person(n, hidden_word, '', ''.join(wrong_words))        
        attempt = input('guess letter\n')
        print(f'you pressed {attempt}')      
        
        if attempt in sel:
            if word.count(attempt) > 1:
                count = hidden_word.count(attempt)            
                pos = sorted(set([word.index(attempt, x) for x in range(len(word)-1)]))[count]                
            else:
                pos = word.index(attempt)            
            hidden_word.pop(pos)
            print(pos)
            hidden_word.insert(word.index(attempt, pos), attempt)
            print(hidden_word, attempt)            
            
            sel.remove(attempt)
            # print(word, ''.join(hidden_word))
        else:
            wrong_words.append(attempt) 
            n+=1

        if n == 7:
            draw_person(n, ''.join(hidden_word), word)
            print('Game over!')
            break
        draw_person(n, ''.join(hidden_word), '', ''.join(wrong_words))
        print('Condragulations, my queen! You won!')

guess_word()
