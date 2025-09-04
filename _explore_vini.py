#%%
import re
import pandas as pd 
from pprint import pprint
import requests
from unidecode import unidecode
#%%
lala = './vini.txt'
# %%
with open(lala, 'r',  encoding="utf8") as _:
    vini = _.read()
# %%
lv = re.findall('/@vinifofini/video/\d*', vini)
#%%
#%%
result = []
for video in lv:
    
    req = requests.get('https://www.tiktok.com/' + video )
    
    res_video = re.findall('@vinifofini/video/\d+","name":(.{,200}TikTok")',req.text)

    if len(res_video) ==1:
        if res_video not in result:
            pprint(res_video)

            
            result.append(res_video)
        
        
# %%
result
# %%
result


# %%
re.findall('@vinifofini/video/\d+","name":(.{,200}TikTok")',req.text)
# %%
xx = '\n'.join(str(x) for x in result)
# %%
len(result)
# %%
dic = []
dic2 = []
for word in re.findall('\w+', xx):
    word = word.lower()
    if word[-1] == 's':
        word = word[-1]
    print(word)
    if word not in dic2:
        dic.append([word, xx.lower().count(word)])
    dic2.append(word)
# %%
sorted(dic, key = lambda x: x[1])
#%%
dic2
# %%
[x for x in result if re.search('auti|asp|via|gay|lgb|ansi|fam|impa|come|^hiper', unidecode(str(x)))]
# %%
result
# %%
