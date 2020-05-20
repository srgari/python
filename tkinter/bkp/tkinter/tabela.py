from tkinter import *
from tkinter import ttk

import pandas as pd 
df = pd.read_csv(f'tabela_teste.csv')
w = Tk()
tree = ttk.Treeview(w)

w.title('Visualisador de csv')

tree["columns"]=('0','1','2','3')
for x,y in zip(('0','1','2','3'),tuple(df.columns)):
    tree.column(x, width=100, minwidth=100, )
    tree.heading(x,text=y)




for x in range(df.shape[0]):
    #tree.insert('',x,str(x), text = 'indice', values = tuple(df.iloc[x].values))
    tree.insert('',x+1,str(x+1), text = 'indice', values = tuple(df.iloc[x].values))


tree.pack()

w.mainloop()
