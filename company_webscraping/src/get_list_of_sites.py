# collected from https://www.twilio.com/blog/asynchronous-http-requests-in-python-with-aiohttp
# aqui a gente pega a lista de sites q existe no site da sinapse. Só isso.

import sys 
sys.path.insert(1,'/home/user/Documents/git/python/company_webscraping/src/')


import aiohttp
import asyncio 
import time 
import os 
import re

curdir = os.path.dirname(__file__)
os.chdir(curdir)
sys.path.append(curdir)

async def __get_list_of_sites(website):

    async with aiohttp.ClientSession() as session:
        async with session.get(website) as response:

            print('Status:', response.status)
            print('Content type:', response.headers['content-type'])

            global html
            html = await response.text()
            print('body:', html[:15], '...')
            title = re.findall('<title>(.*)</title>', html)[0]
            
        

def generate_list_of_sites(website):
    """ Input: the website you wish to scrape. Output: list of embebed websites. """
    loop = asyncio.get_event_loop()
    loop.run_until_complete(__get_list_of_sites(website))    
    l = list(set(re.findall('href="(.*)?/"', html) + [website] ))
    return l

if __name__ == '__main__':
    l = generate_list_of_sites('https://www.sinapsebiotecnologia-loja.com.br')
    print(len(l))
#%%