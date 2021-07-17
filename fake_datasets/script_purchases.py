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

df_m['mercado'] = np.random.choice(['Broa de Açúcar','Plus','Mes'], len(df_m))
df_f['mercado'] = np.random.choice(['Broa de Açúcar','Plus','Plus','Mes'], len(df_f))
#%%
df_m['produto'] = np.random.choice(['maçã','banana','pera','uva'], len(df_m))
df_f['produto'] = np.random.choice(['maçã','banana','banana','pera','pera'], len(df_f))
# %%
df_final = pd.concat([df_m,df_f])[['cpf','mercado','produto']]
# %%
df_final.to_csv('csv/mercados_produtos.csv')
# %%
