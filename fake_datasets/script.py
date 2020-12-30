#%%
## GERANDO DATASET DE DADOS DOS CLIENTES:
## - NOME + SEXO
## - SOBRENOME
## - DATA_NASCIMENTO
## - CPF
## - ENDEREÇO


#%%
import pandas as pd 
import numpy as np
import re 
import requests
from bs4 import BeautifulSoup

np.random.seed(42)
# %%
#### PARTE 1: NOMES E SEXO DOS CLIENTES: #####
### UTILIZANDO O DATASET https://brasil.io/dataset/genero-nomes/files/ 
### DO brasil.io, DO ALVARO JUSTIN
### OBRIGADO, ALVARO!

dataset = pd.read_csv('csv/nomes.csv.gz')
dataset = dataset[['group_name','classification']]
dataset.rename(columns={'group_name':'nome','classification':'sexo'}, inplace = True)
dataset
# %%
#### PARTE 2: SOBRENOMES
### UTILIZANDO SOBRENOMES DE tiltedlogic.org
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
req = requests.get('http://www.tiltedlogic.org/Familia/surnames-all.php?tree=', headers = headers)
soup = BeautifulSoup(req.text)
lista_sobrenomes_simples = [x.text.encode('latin').decode('utf8').strip().upper() for x in soup.find_all('a', {'href':re.compile('mylastname')})][4:]

funcao_ordem_sobrenome_aleatoria = lambda: np.random.choice(lista_sobrenomes_simples, len(lista_sobrenomes_simples), replace = False)

def sobrenome_composto():
    result = set()
    for x in funcao_ordem_sobrenome_aleatoria():
        for y in funcao_ordem_sobrenome_aleatoria():
            if x != y:
                result.add(x + ' ' + y)
            if len(result) == len(dataset):
                return list(result)

dataset.insert(1,'sobrenome', sobrenome_composto())
dataset

#%%
### CPFS: CRIAR CPFS VÁLIDOS

lista_cpfs = [str(x) for x in np.random.randint(300000000,399999999,len(dataset))]

for x in range(len(lista_cpfs)):
    lala = sum([(int(y)*z) for y,z in zip(lista_cpfs[x], range(10,1,-1))])*10%11
    lala = lala if int(lala) < 10 else '0'
    lista_cpfs[x] = lista_cpfs[x] + str(lala)
    lele = str(sum([(int(y)*z) for y,z in zip(lista_cpfs[x], range(11,1,-1))])*10%11)
    lele = lele if int(lele) < 10 else '0'
    lista_cpfs[x] = lista_cpfs[x] + lele

lista_cpfs

# %%
dataset.insert(3, 'cpf', lista_cpfs)
#%%
dataset.insert(0, 'id_cliente', (dataset['nome'] + dataset['sobrenome'] + dataset['cpf']).apply(hash))

#%%
dataset


# %%
dataset.to_csv('csv/dados_clientes.csv', index = False)
# %%
