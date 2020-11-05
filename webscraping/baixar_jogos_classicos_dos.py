'''
baixe jogos clássicos! 
Tudo joguinho da minha infância e adolescência!
Tudo freeware ou shareware, então acho que não é pirataria!
:D
'''

import requests 

print('teste')
for game in ['alleycat']:#,'DOSBOX_BLOOD','DOSBOX_DOOM','DOSBOX_WAR2','DOSBOX_POP']:
	req = requests.get(f'https://www.dosgames.com/files/{game}.zip', 
	allow_redirects = True, headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})

	print(f'baixando {game}')
	with open(f'{game}.zip', 'wb') as x:		
		x.write(req.content)

import os
from zipfile import ZipFile 

for x in os.listdir():
	if '.zip' in x:
		dir_place = x.replace('.zip','').replace('DOSBOX_','')
		if dir_place not in os.listdir(): os.mkdir(dir_place)
		with ZipFile(x, 'r') as zipobj:
			zipobj.extractall(dir_place)

