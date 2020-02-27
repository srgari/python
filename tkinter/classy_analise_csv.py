import tkinter as tk, pandas as pd
from tkinter import ttk
import os
from PIL import ImageTk, Image
import matplotlib.pyplot as plt

class OOP():
    
    def __init__(self):
        self.w = tk.Tk()
        self.tree = ttk.Treeview(self.w)
        self.escolha_arquivo()

    #================================
    # Parte da escolha do arquivo
    #================================
    def escolha_arquivo(self):
        ttk.Label(self.w, text = "Escolha o arquivo").grid(column = 1, row = 0)
        self.arquivo_escolhido = ttk.Combobox(self.w, width = 50)
        self.arquivo_escolhido['values'] = tuple([x for x in os.listdir() if '.csv' in x])
        self.arquivo_escolhido.grid(column=1, row = 1)
        self.arquivo_escolhido.current(0)
        self.b_arquivo_selecionado = ttk.Button(self.w, text = 'Pressione após escolher', command = self.escolha_colunas)
        self.b_arquivo_selecionado.grid(column = 1, row = 2)


    #================================
    # Parte da escolha das colunas
    #================================

    def escolha_colunas(self):
        self.tabela = self.arquivo_escolhido.get()
        self.df = pd.read_csv(self.tabela)
        self.df = self.df[[x for x in self.df.columns if 'Unnamed' not in x]]
        for x in self.df.columns:
            if 'data' in x.lower():
                self.df[x] = pd.to_datetime(self.df[x])
        self.t_colunas = tuple(self.df.columns)

        ttk.Label(self.w, text = self.tabela).grid(column = 0, row = 0)
        ttk.Label(self.w, text = 'Coluna categórica').grid(column = 4, row = 1)
        self.e_categorica = ttk.Combobox(self.w, width = 40,)
        self.e_categorica['values'] = self.t_colunas
        self.e_categorica.grid(column = 5, row = 1)
        self.e_categorica.current(1)
        
        ttk.Label(self.w, text = 'Coluna numérica').grid(column = 4, row = 2)
        self.e_numerica = ttk.Combobox(self.w, width = 40,)
        self.e_numerica['values'] = self.t_colunas
        self.e_numerica.grid(column = 5, row = 2)
        self.e_numerica.current(3)

        ttk.Label(self.w, text = 'Coluna data').grid(column = 4, row = 3)
        self.e_data = ttk.Combobox(self.w, width = 40,)
        self.e_data['values'] = self.t_colunas
        self.e_data.grid(column = 5, row = 3)
        self.e_data.current(0)

        ttk.Button(self.w, text = 'Selecionar colunas', command = self.resultados).grid(column = 4, row = 4)

            #=====================================
            # Fim da parte da escolha das colunas
            #=====================================


    #===================================
    # Parte dos resultados estatísticos
    #===================================

    def analisador_tabela(self): 
        self.est_categorias = self.df.groupby(self.categorica)[self.quantitativa].agg(['sum','mean','std','min','max']).T
        self.est_todos = self.df[self.quantitativa].agg(['sum','mean','std','min','max']).rename(columns = {self.quantitativa:'todos'})
        self.df_estatistica = pd.concat([self.est_categorias,self.est_todos], axis = 1).rename(columns = {0:'todos'})
        return self.df_estatistica.applymap(lambda x: f'{round(x):,}')

    def resultados(self):
        self.categorica = self.e_categorica.get()
        self.quantitativa = self.e_numerica.get()
        self.dataevento = self.e_data.get()
        
        self.df_e = self.analisador_tabela()

        self.n_colunas = tuple([str(x) for x in range(len(self.df_e.columns))])

        self.tree["columns"]=self.n_colunas
        for x,y in zip(self.n_colunas,tuple(self.df_e.columns)):
            self.tree.column(x, width=100, minwidth=100, anchor = tk.CENTER)
            self.tree.heading(x,text=y)

        for x in range(self.df_e.shape[0]): self.tree.insert('',x+1,str(x+1), text = self.df_e.index[x], values = tuple(self.df_e.iloc[x].values))


        self.tree.grid(column = 1, row = 5,columnspan = 4)


        self.df_plot = self.df.groupby([self.categorica,pd.Grouper(key = self.dataevento, freq = 'M')])\
        .qtd_vendida.sum().reset_index()\
        .pivot_table(index = self.dataevento, columns = self.categorica, values = self.quantitativa)\
        
        self.plot = self.df_plot.plot(figsize = [8,4])
        plt.title('vendas por mês')
        self.fig = self.plot.get_figure()
        
        self.fig.savefig('place_holder.png')

        self.load = Image.open('place_holder.png')
        self.render = ImageTk.PhotoImage(self.load)
        self.img = ttk.Label(self.w, image = self.render)
        self.img.image = self.render
        self.img.grid(column = 1, row = 6, columnspan = 4)

        #==========================================
        # Fim da parte dos resultados estatísticos
        #==========================================

        #====================================
        # Fim da parte da escolha do arquivo
        #====================================


oop = OOP()
oop.w.mainloop()