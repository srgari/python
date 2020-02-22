# importar bibliotecas
import tkinter, subprocess, numpy as np, os
import tkinter.messagebox
import os

w = tkinter.Tk()
w.geometry("600x600")


l = ['steam://rungameid/678950', 
    'steam://rungameid/376300',
    'steam://rungameid/310950']

# importar imagem
icon = tkinter.PhotoImage(file =r'E:\Users\Sergio\OneDrive\Python\batman.png')
label = tkinter.Label(w, image = icon)
label.grid(row = 0, column = 0)

# escolher jogo aleatório para jogar
w.title('Sergio')
def fight():
    x = np.random.choice(l)
    os.system(f'steam {x}')
    tkinter.Label(w, text = np.random.choice(l)).grid(row = 4, column  = 2)
tkinter.Button(w, text = 'luta', command = fight).grid(row = 1, column = 0)

# ver pagina do reddit do ippo
def ippo():
    os.system('chrome https://www.reddit.com/r/hajimenoippo/')
tkinter.Button(w, text = 'Ippo', command = ippo).grid(row = 2, column = 0)

# elogio aleatório
def random_compliment():
    l = ['I like you', 'you can do it!','you are golden!']
    tkinter.Label(w, text = np.random.choice(l)).grid(row = 5, column = 1)
tkinter.Button(w, text = 'Compliment', command = random_compliment).grid(row = 3, column = 0)


# mensagem de atenção
tkinter.messagebox.showinfo('hello!','is it me you are looking for?')

# mensagem que pede sim ou não
response = tkinter.messagebox.askquestion('I can see it in your eyes')
if response == 'yes':
    tkinter.Label(w, text = 'yes').grid(row = 5, column = 0)
else:
    tkinter.Label(w, text = str(response)).grid(row = 2)

# caixa de texto
e = tkinter.Entry(master = w)
e.grid(row = 6)
e.insert(0, 'digite algo aqui')

def get_text(entry = 0):
    s = e.get()
    tkinter.Label(w,text = f'você digitou {s}').grid(row = 7)

w.bind('<Return>', get_text)

w.mainloop()
