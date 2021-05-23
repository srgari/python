###########################################
### agora o bicho pega 
### pegar todos os htmls de todas as páginas e juntar em um só
##########################################

import sys 
sys.path.insert(1,'/home/user/Documents/git/python/company_webscraping/src/')


from get_list_of_sites import *
import numpy as np

async def __get_site(session, url):
    async with session.get(url) as resp:
        html = await resp.text()        
        title = re.findall('<title>(.*)</title>', html)

        # if len(title) > 0:
        #     print(f'saving html {title}')
        #     with open(title[0].replace('/','_')+'.html', 'w') as x:
        #         x.write(html)
        list_of_htmls.append('\n\n\n\n#########################' + html + '\n\n\n\n###############################')         


async def __put_get_site_function_on_queue():

    async with aiohttp.ClientSession() as session:
        
        tasks = []
        for url in l:
            print(f'\nconnecting to {url}\n')
            tasks.append(asyncio.ensure_future(__get_site(session, url)))
        
        original_site = await asyncio.gather(*tasks)
        

def get_all_htmls(website: str) -> list:
    """Input: your desired website. Output: list of all html of embebed links """
    global list_of_htmls
    list_of_htmls = []
    s = time.time()
    global l
    l = generate_list_of_sites(website)
    asyncio.run(__put_get_site_function_on_queue())
    e = time.time()
    print(f'ftime: {(e-s):.2f}')
    return list_of_htmls

def save_list_of_htmls_as_txt():
    with open('final_text.txt', 'w') as x:
        x.write('\n\n\n\n'.join(html))


if __name__ == '__main__':
    x = get_all_htmls('https://www.sinapsebiotecnologia-loja.com.br')
    print(type(x), len(x))
    