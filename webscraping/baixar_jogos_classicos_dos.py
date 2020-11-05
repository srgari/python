'''
baixe jogos clássicos! 
Tudo joguinho da minha infância e adolescência!
Tudo freeware ou shareware (eu acho :P), então acho que não é pirataria!
:D
'''

# biblioteca que baixa o conteúdo da internet
import requests 
# header: pro site achar que o código é um navegador
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# baixar uma penca de jogos do site dosgames: jogos na lista 
for game in ['alleycat.zip','DOSBOX_BLOOD.ZIP','DOSBOX_DOOM.ZIP','DOSBOX_WAR2.ZIP','DOSBOX_POP.ZIP']:
	req = requests.get(f'https://www.dosgames.com/files/{game}', 
	headers = headers)

	print(f'baixando {game}')
	# essa parte salva o conteúdo como um arquivo binário do tipo zip
	with open(f'{game}.zip', 'wb') as x:		
		x.write(req.content)

# Baixar worms do site dosgamesarchime (daria pra baixar vários daqui tbm)
req2 = requests.get('https://image.dosgamesarchive.com/games/worms.zip',
	headers = headers)

# essa parte salva o conteúdo como um arquivo binário do tipo zip
with open('worms.zip' ,'wb') as x:
	x.write(req2.content)
	
# biblioteca que deixa criar e acessar pastas
import os

# biblioteca que dezipa arquivos
from zipfile import ZipFile 

#mandar dezipar na pasta do jogo tudo que é zip
for x in os.listdir():
	if '.zip' in x:
		dir_place = x.replace('.zip','').replace('DOSBOX_','')
		if dir_place not in os.listdir(): os.mkdir(dir_place)
		with ZipFile(x, 'r') as zipobj:
			zipobj.extractall(dir_place)

