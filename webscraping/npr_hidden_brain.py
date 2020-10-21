#%%
import requests
from bs4 import BeautifulSoup
import re
#%%
header = {'ACCEPT':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
baseURL = 'https://www.npr.org/series/423302056/hidden-brain/archive?date=9-30-2020'
req = requests.request('GET', baseURL, headers = header, data = {})


soup = BeautifulSoup(req.text)
#%%


# %%
lala = [str(x) for x in soup.find_all('a')]

# pegar os links apenas:
[re.findall(r'href="(.*)">',x) for x in lala if re.search('npr.org/[\d]{4}/',x) and len(re.findall('href="(.*)>$',x)) >0]

# %%
req.headers
# %% Continuar depois
