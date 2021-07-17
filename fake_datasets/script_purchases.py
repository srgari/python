#%%
import pandas as pd
import numpy as np
link = 'https://raw.githubusercontent.com/srgari/python/master/fake_datasets/csv/dados_clientes.csv'

#%%
df = pd.read_csv(link)
# %%
df
# %%
df.cpf
# %%
df2 = df[['cpf','sexo','uf']]
# %%
df_m = df2.query('uf == "SP" & sexo == "M"').sample(200)
df_f = df2.query('uf == "SP" & sexo == "F"').sample(180)
# %%

df_m = df_m.sample(2000, replace = True)
df_f = df_f.sample(2000, replace = True)

#%%
df_m['nome'] = np.random.choice(['Broa de Açúcar','Plus','Mes'], len(df_m))
df_f['nome'] = np.random.choice(['Broa de Açúcar','Plus','Plus','Mes'], len(df_f))
#%%
df_m['produto'] = np.random.choice(['maçã','banana','pera','uva'], len(df_m))
df_f['produto'] = np.random.choice(['maçã','banana','banana','pera','pera'], len(df_f))
df_m['data'] = np.random.choice(pd.date_range('2021-01-01','2021-01-31'), len(df_m))
df_f['data'] = np.random.choice(pd.date_range('2021-01-01','2021-01-31'), len(df_m))

# %%
df_final = pd.concat([df_m,df_f])[['cpf','nome','produto','data']]

dic_preco = {
    'maçã':2,
    'banana':1,
    'pera':3,
    'uva':7
}
df_final['preco'] = df_final['produto'].map(dic_preco)
# %%
df_final.to_csv('csv/venda_produtos.csv')
# %%
df_final
# %%
df_final.head(2)
# %%
