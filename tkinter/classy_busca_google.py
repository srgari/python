# 1- importar bibliotecas

from tkinter import *
import os

class OOP():
	def __init__(self):
		# 2- gerar janela principal; definir tamanho; dar nome
		self.w = Tk()
		self.w.geometry('300x300')
		self.w.title('Busca google')
		self.my_widgets()

	def my_widgets(self):
		# 3.4- ativar busca ao pressionar Enter
		self.w.bind('<Return>', self.x)

		# 3.5 - criar botão de busca
		Button(self.w, text = 'Estou me sentindo com sorte!', command = self.x).pack()

		# 3- fazer buscas no chrome
		# 3.1 - definir diretório para o do chrome
		os.chdir("\Program Files (x86)\Google\Chrome\Application")

		# 3.2- criar campo de busca

		self.e = Entry(master = self.w)
		self.e.pack()
		self.e.insert(0,'Busca google')

		# 3.3- criar função que coleta texto
	def x(self, event = 0):
		'''Função coletadora de texto. Event=0 é requisitado por w.bind abaixo'''
		self.s = self.e.get()
		Label(self.w, text = self.s).pack()
		os.system(f'chrome "? {self.s}"')
		# 4- botar programa para rodar em loop eterno

oop = OOP()

oop.w.mainloop()
