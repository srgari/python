# importar bibliotecas
import tkinter as tk, numpy as np, os
from tkinter import ttk
import tkinter.messagebox
import os

w = tk.Tk()
w.geometry("400x200")

ttk.Label(w, text = 'Deixe o botão escolher um jogo aleatório', font = "arial, 14").grid(row = 0, column = 1)

# escolher jogo aleatório para jogar
w.title('Sergio')
def fight():
    l = ['steam://rungameid/678950', 
    'steam://rungameid/376300',
    'steam://rungameid/310950']

    x = np.random.choice(l)
    os.system(f'steam {x}')    
tk.Button(w, text = 'luta', command = fight).grid(row = 1, column = 1)



def action2d():
    l = ['steam://rungameid/200900',
'steam://rungameid/250760',
'steam://rungameid/363440',
'steam://rungameid/367520',
'steam://rungameid/428550',
'steam://rungameid/504230',
'steam://rungameid/553640',
'steam://rungameid/743890',
'steam://rungameid/916730',
]

    x = np.random.choice(l)
    os.system(f'steam {x}')    
tk.Button(w, text = 'ação2d', command = action2d).grid(row = 2, column = 1)




d ={
"Rogue Legacy": "241600", 
"Cave Story+": "200900", 
"Dragon Ball Fighterz": "678950", 
"Mega Man Legacy Collection": "363440", 
"Mega Man X Legacy Collection": "743890", 
"Out There Somewhere": "263980", 
"Icey": "553640", 
"Street Fighter V": "310950", 
"Doom 2016": "379720", 
"Counter Strike GO": "730", 
"Mean Greens Plastic Warfare": "360940", 
"Hotline Miami": "219150", 
"Faster Than Light": "212680", 
"Hollow Knight": "367520", 
"Half Life": "70", 
"Final Doom": "2290",
"Ultimate Doom":"2280",
"Super Mario Bros X": "14750106498495414272",
"Sonic Chaos": "10324995912400633856",
"Sonic 3 AIR": "10309753391294709760",}


keys = list(d.keys())
values = list(d.values())


def random_random():
    x = np.random.choice(values)
    os.system(f'steam  steam://rungameid/{x}')    
tk.Button(w, text = 'random_random', command = random_random).grid(row = 3, column = 1)





# Combo box widgets
ttk.Label(w, text = '', font = 'arial, 11').grid(column = 1, row = 4)
ttk.Label(w, text = 'Ou escolha um jogo da lista:', font = 'arial, 13').grid(column = 1, row = 5)
game = tk.StringVar()
game_selected = ttk.Combobox(w, width = 30, textvariable = game, state = 'readonly')
game_selected['values'] = keys
game_selected.grid(column = 1, row = 6)
game_selected.current(5)

def  selected_game():
    ttk.Label(w, text = f'você escolheu: {game_selected.get()}').grid(column = 1, row = 7)
    ttk.Label(w, text = f'steam steam://rungameid/{d[game_selected.get()][0]}').grid(column = 1, row = 8 )
    os.system(f'steam steam://rungameid/{d[game_selected.get()]}')
ttk.Button(w, text = 'clique aqui', command = selected_game).grid(column = 1, row = 9)

# elogio aleatório
# w.counter = 0
# ttk.Label(w, text = 'Ou receba uma frase motivacional, em inglês', font = 'arial, 14').grid(column = 1, row = 7)
# def random_compliment():
#     if w.counter < 10:
#         l = ['I like you', 'you can do it!','you are golden!',
#         'you are terrific!',
#         'you brighten my day',
#         'you are my sunshine']
#         tk.Label(w, text = f'                                                                  ',  font=("Helvetica", 16)).grid(row = 8, column = 1,)
#         tk.Label(w, text = np.random.choice(l),  anchor = 'e', font=("Helvetica", 16)).grid(row = 9, column = 1)
#         w.counter = w.counter + 1
#     else:
#         l = ["that's enough for today",
#         "It doesn't get any better than this!",
#         "Enjoying yourself?"]
#         tk.Label(w, text = '                                                               ',font=("Helvetica", 16)).grid(row = 8, column = 1)
#         tk.Label(w, text = np.random.choice(l),font=("Helvetica", 16)).grid(row = 8, column = 1)

# tk.Button(w, text = f'compliment', command = random_compliment).grid(row = 8, column = 1)



w.mainloop()
