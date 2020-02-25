import tkinter as tk, pandas as pd
from tkinter import ttk
import os
from PIL import ImageTk, Image

# Criação da janela e da árvore (tabela)
w = tk.Tk()
tree = ttk.Treeview(w)

#================================
# Parte da escolha do arquivo
#================================

ttk.Label(w, text = "Escolha o arquivo").grid(column = 1, row = 0)
arquivo_escolhido = ttk.Combobox(w, width = 50)
arquivo_escolhido['values'] = tuple([x for x in os.listdir() if '.csv' in x])
arquivo_escolhido.grid(column=1, row = 1)
arquivo_escolhido.current(0)


def escolha_colunas():
    #================================
    # Parte da escolha das colunas
    #================================

        #===================================
        # Parte dos resultados estatísticos
        #===================================
    def resultados():
        categorica = e_categorica.get()
        quantitativa = e_numerica.get()
        dataevento = e_data.get()
        def analisador_tabela(): 
            est_categorias = df.groupby(categorica)[quantitativa].agg(['sum','mean','std','min','max']).T
            est_todos = df[quantitativa].agg(['sum','mean','std','min','max']).rename(columns = {quantitativa:'todos'})
            df_estatistica = pd.concat([est_categorias,est_todos], axis = 1).rename(columns = {0:'todos'})
            return df_estatistica.applymap(lambda x: f'{round(x):,}')
        df_e = analisador_tabela()

        n_colunas = tuple([str(x) for x in range(len(df_e.columns))])

        tree["columns"]=n_colunas
        for x,y in zip(n_colunas,tuple(df_e.columns)):
            tree.column(x, width=100, minwidth=100, anchor = tk.CENTER)
            tree.heading(x,text=y)

        for x in range(df_e.shape[0]): tree.insert('',x+1,str(x+1), text = df_e.index[x], values = tuple(df_e.iloc[x].values))


        tree.grid(column = 1, row = 5,columnspan = 4)

        #==========================================
        # Fim da parte dos resultados estatísticos
        #==========================================

        df_plot = df.groupby([categorica,pd.Grouper(key = dataevento, freq = 'M')])\
        .qtd_vendida.sum().reset_index()\
        .pivot_table(index = dataevento, columns =categorica, values = quantitativa)\

        plot = df_plot.plot()
        fig = plot.get_figure()
        fig.savefig('place_holder.png')

        load = Image.open('place_holder.png')
        render = ImageTk.PhotoImage(load)
        img = ttk.Label(w, image = render)
        img.image = render
        img.grid(column = 1, row = 6)





    tabela = arquivo_escolhido.get()
    df = pd.read_csv(tabela)
    df = df[[x for x in df.columns if 'Unnamed' not in x]]
    for x in df.columns:
        if 'data' in x.lower():
            df[x] = pd.to_datetime(df[x])

    t_colunas = tuple(df.columns)
        

    ttk.Label(w, text = tabela).grid(column = 0, row = 0)

    ttk.Label(w, text = 'Coluna categórica').grid(column = 4, row = 1)
    e_categorica = ttk.Combobox(w, width = 40,)
    e_categorica['values'] = t_colunas
    e_categorica.grid(column = 5, row = 1)
    e_categorica.current(1)
    
    ttk.Label(w, text = 'Coluna numérica').grid(column = 4, row = 2)
    e_numerica = ttk.Combobox(w, width = 40,)
    e_numerica['values'] = t_colunas
    e_numerica.grid(column = 5, row = 2)
    e_numerica.current(3)

    ttk.Label(w, text = 'Coluna data').grid(column = 4, row = 3)
    e_data = ttk.Combobox(w, width = 40,)
    e_data['values'] = t_colunas
    e_data.grid(column = 5, row = 3)
    e_data.current(0)

    ttk.Button(w, text = 'Selecionar colunas', command = resultados).grid(column = 4, row = 4)

    #=====================================
    # Fim da parte da escolha das colunas
    #=====================================


b_arquivo_selecionado = ttk.Button(w, text = 'Pressione após escolher', command = escolha_colunas)
b_arquivo_selecionado.grid(column = 1, row = 2)


#====================================
# Fim da parte da escolha do arquivo
#====================================


w.mainloop()