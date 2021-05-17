#%%

### CONTINUANDO COM OS TESTES
### LOG DE MUDANÇAS (IGNORANDO AS ANTIGAS):
### -2021/1/9 03:24 - sergio_linux
### -2021/1/14 1:15 - sergio_windows
 
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
import re
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

#%% CPFS: CRIAR CPFS VÁLIDOS

lista_cpfs = [str(x) for x in np.random.randint(300000000,399999999,len(dataset))]

for x in range(len(lista_cpfs)):
    lala = sum([(int(y)*z) for y,z in zip(lista_cpfs[x], range(10,1,-1))])*10%11
    lala = lala if int(lala) < 10 else '0'
    lista_cpfs[x] = lista_cpfs[x] + str(lala)
    lele = str(sum([(int(y)*z) for y,z in zip(lista_cpfs[x], range(11,1,-1))])*10%11)
    lele = lele if int(lele) < 10 else '0'
    lista_cpfs[x] = lista_cpfs[x] + lele

#lista_cpfs

# %%
dataset.insert(3, 'cpf', lista_cpfs)
dataset
#%%
dataset.insert(0, 'id_cliente', (dataset['nome'] + dataset['sobrenome'] + dataset['cpf']).apply(hash))

#%%
### GRAU ESCOLARIDADE (BASEADO EM LISTA DE 2016)
### fonte:https://agenciadenoticias.ibge.gov.br/agencia-sala-de-imprensa/2013-agencia-de-noticias/releases/18992-pnad-continua-2016-51-da-populacao-com-25-anos-ou-mais-do-brasil-possuiam-no-maximo-o-ensino-fundamental-completo
'''
11,2% não tinham instrução; 
30,6% fundamental incompleto; 
9,1% fundamental completo; 
3,9% tinham ensino médio incompleto; 
26,3% tinham o ensino médio completo e 
15,3% o superior completo
'''
l = ['sem instrucao']*112 + \
['fundamental incompleto']*306 + \
['fundamental completo']*91 + \
['ensino medio incompleto']*39 +\
['ensino medio completo']*263 +\
['superior completo']*153

lista_instrucao = np.random.choice(l, len(dataset))
[(x, l.count(x)/len(l)) for x in set(l)]

dataset.insert(5, 'grau_instrucao', lista_instrucao)


# %%
### CEP
## https://www.correios.com.br/enviar-e-receber/ferramentas/cep/estrutura-do-cep
### CRIAR CEP DE ACORDO COM O CPF
## (NÚMERO 9 DO CPF: REGIÃO; PRIMEIRO DÍGITO CEP: REGIÃO)
    
cep = '''
CEP Região Sudeste 01000-000 a 39999-999
São Paulo(SP) 01000-000 a 19999-999
Rio de Janeiro(RJ) 20000-000 a 28999-999
Espírito Santo(ES) 29000-000 a 29999-999
Minas Gerais(MG) 30000-000 a 39999-999
 
CEP Região Nordeste 40000-000 a 65999-999
Bahia(BA) 40000-000 a 48999-999
Sergipe(SE) 49000-000 a 49999-999
Pernambuco(PE) 50000-000 a 56999-999
Alagoas(AL) 57000-000 a 57999-999
Paraíba(PB) 58000-000 a 58999-999
Rio Grande do Norte(RN) 59000-000 a 59999-999
Ceará(CE) 60000-000 a 63999-999
Piauí(PI) 64000-000 a 64999-999
Maranhão(MA) 65000-000 a 65999-999
 
CEP Região Norte
Pará(PA) 66000-000 a 68899-999
Amapá(AP) 68900-000 a 68999-999
Amazonas(AM) 1 69000-000 a 69299-999
Roraima(RR) 69300-000 a 69399-999
Amazonas(AM) 2 69400-000 a 69899-999
Acre(AC) 69900-000 a 69999-999
Rondônia(RO) 76800-000 a 76999-999
Tocantins(TO) 77000-000 a 77999-999
 
CEP Região Centro-Oeste
Distrito Federal(DF) 1 70000-000 a 72799-999
Goiás(GO) 1 72800-000 a 72999-999
Distrito Federal(DF) 2 73000-000 a 73699-999
Goiás(GO) 2 73700-000 a 76799-999
Mato Grosso(MT) 78000-000 a 78899-999
Mato Grosso do Sul(MS) 79000-000 a 79999-999
CEP Região Sul 80000-000 a 99999-999
Paraná(PR) 80000-000 a 87999-999
Santa Catarina(SC) 88000-000 a 89999-999
Rio Grande do Sul(RS) 90000-000 a 99999-999
'''
dic_cep = dict()
dic_uf_nome = dict()
for x in cep.split('\n'):
    if '(' in x: 
        cep_str = re.findall('\d+-\d+',x)
        cep_int = [int(x.replace('-','')) for x in cep_str]
        nome = re.findall('[A-zÀ-ÿ\s]+',x)[0]
        uf = re.findall('[A-zÀ-ÿ\s]+',x)[1]
        dic_uf_nome[uf] = nome
        dic_cep[uf] = cep_int


dic_cep

#%%
### ADICIONAR CEP CERTO POR CPF
### FONTE: https://pt.wikipedia.org/wiki/Cadastro_de_pessoas_f%C3%ADsicas
cpf_estado = '''
1:DF GO MT MS TO
2:AC AP AM PA RO RR
3:CE MA PI
4:AL PB PE RN
5:BA SE
6:MG
7:ES RJ
8:SP
9:PR SC
0:RS
'''

lista_cpf = cpf_estado.split('\n')
lista_cpf2 = [y.split(':') for y in lista_cpf if len(y) > 1] 
lista_cpf3 = [(x,y.split()) for x,y in lista_cpf2]

dic_cpf = {x:y for x,y in lista_cpf3}
func_cpf = lambda x: np.random.choice(dic_cpf[x])
func_cpf('1')

#%% ADICIONAR UF
serie_uf = dataset.cpf.str[-3].map(func_cpf)
dataset.insert(6,'uf', serie_uf)

#%% ADICIONAR CEP
def lala(x):
    lele = np.random.randint(dic_cep[x][0],dic_cep[x][1])
    lele = str(lele).rjust(8,'0')
    lele = lele[:5] + '-' + lele[5:]
    return lele
lala('SP')

serie_cep = dataset.uf.map(lala)
serie_cep
dataset.insert(7,'cep', serie_cep)
#%% ADICIONAR IDADE
dataset['idade'] = np.random.normal(30,10,len(dataset))
dataset.loc[dataset['idade'] < 10, 'idade'] = dataset.loc[dataset['idade'] < 20]['idade'] + 20
dataset.loc[dataset['idade'] < 20, 'idade'] = dataset.loc[dataset['idade'] < 20]['idade'] + 10
dataset.loc[dataset['idade'] > 80, 'idade'] = dataset.loc[dataset['idade'] > 80]['idade'] - 10

#%%
dataset.to_csv('csv/dados_clientes.csv', index = False)
# %%
dataset
# %%
### MUDANÇA BESTA 2: TESTANDO GIT DIFF
### DE NOVO: DESSA VEZ, VÊ SE SÓ FAZ O GIT ADD, SUA MULA!