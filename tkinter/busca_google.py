# 1- importar bibliotecas

from tkinter import *
import os

# 2- gerar janela principal; definir tamanho; dar nome
w = Tk()
w.geometry('300x300')
w.title('Busca google')

# 3- fazer buscas no chrome
# 3.1 - definir diretório para o do chrome
os.chdir("\Program Files (x86)\Google\Chrome\Application")

# 3.2- criar campo de busca

e = Entry(master = w)
e.pack()
e.insert(0,'Busca google')

# 3.3- criar função que coleta texto
def x(event = 0):
	'''Função coletadora de texto. Event=0 é requisitado por w.bind abaixo'''
	s = e.get()
	Label(w, text = s).pack()
	os.system(f'chrome "? {s}"')

# 3.4- ativar busca ao pressionar Enter
w.bind('<Return>', x)

# 3.5 - criar botão de busca
Button(w, text = 'Estou me sentindo com sorte!', command = x).pack()

# 4- botar programa para rodar em loop eterno
w.mainloop()
