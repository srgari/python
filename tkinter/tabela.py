from tkinter import *
from tkinter import ttk

import pandas as pd 
df = pd.read_csv('tabela_teste.csv')
w = Tk()
tree = ttk.Treeview(w)

w.title('Visualisador de csv')

tree["columns"]=('0','1','2','3')
for x,y in zip(('0','1','2','3'),tuple(df.columns)):
    tree.column(x, width=100, minwidth=100, )
    tree.heading(x,text=y)
# tree.column("one", width=150, minwidth=150, )
# tree.column("two", width=400, minwidth=200)
# tree.column("three", width=80, minwidth=50, )

# tree.heading("#0",text="Name")
# tree.heading("one", text="Date modified")
# tree.heading("two", text="Type")
# tree.heading("three", text="Size")


# Level 1

for x in range(df.shape[0]):
    #tree.insert('',x,str(x), text = 'indice', values = tuple(df.iloc[x].values))
    tree.insert('',x+1,str(x+1), text = 'indice', values = tuple(df.iloc[x].values))

# Level 2

tree.pack()

w.mainloop()
