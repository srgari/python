#!/home/user/.pyenv/versions/3.9.4/bin/python

### Aki a gente faz ETL, extrai dados e gera o HTML

# from get_html_of_sites import get_all_htmls

import sys 
import pandas as pd
sys.path.append('/home/user/Documents/git/python/company_webscraping/src/')

from get_html_of_sites import *

def __generate_new_html_file():
    html_list = get_all_htmls('https://www.sinapsebiotecnologia-loja.com.br')
    
    return html_list


# %% with price:
def generate_price_table():
    html_list = __generate_new_html_file()
    
    html = '\n\n\n\n\n#############\n#############\n#############'.join(html_list)
    pattern1 = re.compile("<div class=\"informacoesListagemPrincipais\">.*\n.*\n.*<p>(.*)</p>.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*>(.*)<")

    products_price = set(re.findall(pattern1,html))
    

    # %% without price:
    pattern2 = re.compile("<div class=\"informacoesListagemPrincipais\">.*\n.*\n.*<p>(.*)</p>")

    products = list(set(re.findall(pattern2,html)))
    
    df1 = pd.DataFrame(products, columns = ['name'])

    df2 = pd.DataFrame(products_price, columns = ['name','price'])

    df = pd.merge(left = df1, right = df2, on = 'name', how = 'outer')
    return df
    
def generate_html_table():
    df = generate_price_table()
    with open('tabela_sinapse.html', 'w') as x:
        x.write(df.to_html())

if __name__ == '__main__':
    df = generate_price_table()
    with open('tabela_sinapse.html', 'w') as x:
        x.write(df.to_html(index = False))
    df.to_csv('tabela_sinapse.csv', index = False)
    