#%%
import pandas as pd 
from unidecode import unidecode
import numpy as np 
import re 
pd.options.display.max_colwidth = 400
file = './Base de Prontuário e Dicionario.xlsx'
ls = pd.ExcelFile(file).sheet_names
ls
# %%
df_p = pd.read_excel(file, sheet_name = ls[0]) # prontuario
df_d = (
    pd.read_excel(file,  sheet_name = ls[1]) # dicionario
        .assign(DESCRICAO_CID = lambda x: x['DESCRICAO_CID'].apply(unidecode).str.lower())         
        )
df_r = pd.read_excel(file, sheet_name = ls[2]) # resposta ideal
# %% # o dicionário da anamnese do jeito que tá perde coisa
pre_dic = {
    'agud.':'[a-z]{0,}',
    'dor':'(dor|dores)',
    'abdominal':' (abdominal|abdominais)',
    'episodio depressivo':'(depressao|depressivo)',
    'essencial':'(essencial|arterial)',
}

# dicionário da anamnese, tratado com o pre-dicionario acima
dic = (
    df_d
    .assign(
        DESCRICAO_CID = lambda x: x['DESCRICAO_CID'].replace(pre_dic, regex = True)
        )
    .set_index('DESCRICAO_CID')
    ['CID']
    .to_dict())

# funcao que cria coluna q tem o cid. É só especificar a coluna q tem a descricao 
def lala(col): return (
    col
    .str.lower()
    .apply(unidecode)
    .str.replace('.','', regex = False)
    .replace(dic, regex = True)
    .str.replace('[a-z\s,\-\(\)]',' ', regex = True)
    .str.replace('\s+',' ', regex = True)
    .str.strip()
    .apply(lambda x: ', '.join(sorted(set(x.split(' ')))))
    .replace('', pd.NA)    
    )

# criando as colunas q vc precisa
df_p['CID_ANAMNESE'] = lala(df_p['ANAMNESE'])
df_p['CID_PRINCIPAL'] = lala(df_p['EVOLUCAO_MEDICA'])
df_p['CID_PRINCIPAL'] = np.where(df_p['CID_PRINCIPAL'].notna(), df_p['CID_PRINCIPAL'], df_p['CID_ANAMNESE'])
df_p.to_excel('lala.xlsx', index = False)
# %% pra ver cada linha por vez
df_p.loc[7].to_frame()
# %%
