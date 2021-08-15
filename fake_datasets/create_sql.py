#%%
import sqlite3
import pandas as pd 
# %%
conn = sqlite3.connect('tables/fake_datasets.db')
# %%
df_clientes = pd.read_csv('tables/dados_clientes.csv')
df_produtos = pd.read_csv('tables/venda_produtos.csv')

#%%
df_clientes.to_sql('dim_clientes',conn, if_exists = 'replace')
df_produtos.to_sql('dim_vendas',conn, if_exists = 'replace')
# %%
df_produtos
# %%
df_clientes
# %%
