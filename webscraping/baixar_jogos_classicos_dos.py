
#%%
'''
baixe jogos clássicos! 
Tudo joguinho da minha infância e adolescência!
Tudo freeware ou shareware (eu acho :P), então acho que não é  pirataria!

De quebra, adicionei o windows 3.1 já instalado! (dá uns bugs, mas dá pra viver...)
:D
'''
teste = False
# biblioteca que baixa o conteúdo da internet
import requests 
# biblioteca que deixa criar e acessar pastas
import os
# biblioteca que dezipa arquivos
from zipfile import ZipFile 

# setar pasta padrão (linux)
from os.path import expanduser
home = expanduser("~")
os.chdir(f'{home}/Documentos/games')
os.listdir()
#%%
# header: pro site achar que o código é um navegador
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# baixar uma penca de jogos do site dosgames: jogos na lista 
def baixar_jogos():
	for game in ['alleycat.zip',
				'DOSBOX_BLOOD.ZIP',
				'DOSBOX_DOOM.ZIP',
				'DOSBOX_WAR2.ZIP',
				'DOSBOX_POP.ZIP',
				'jill1.zip',
				'DOSBOX_KEEN.ZIP'
				]:
		req = requests.get(f'https://www.dosgames.com/files/{game}', 
		headers = headers)

		print(f'baixando {game}')
		# essa parte salva o conteúdo como um arquivo binário do tipo zip
		with open(f'{game.lower()}', 'wb') as x:		
			x.write(req.content)

	# Baixar worms do site dosgamesarchime (daria pra baixar vários daqui tbm)
	req2 = requests.get('https://image.dosgamesarchive.com/games/worms.zip',
		headers = headers)

	# essa parte salva o conteúdo como um arquivo binário do tipo zip
	with open('worms.zip' ,'wb') as x:
		x.write(req2.content)

if teste == False: baixar_jogos()
#%%
### BAIXAR O WINDOWS 3.1
def baixar_windows():
	print('baixando windows 3.1')
	win_link = 'https://archive.org/download/msdos_win3_1/win31.zip'
	req3 = requests.get(win_link, headers = headers)
	with open('win31.zip', 'wb') as x:
		x.write(req3.content)

if teste == False: baixar_windows()
#%%

#mandar dezipar na pasta do jogo tudo que é zip; ignorar o windows 3.1
def dezipar_jogos():
	for x in os.listdir():
		if '.zip' in x and 'win31' not in x:
			dir_place = x.replace('.zip','').replace('dosbox_','')
			if dir_place not in os.listdir(): os.mkdir(dir_place)
			with ZipFile(x, 'r') as zipobj:
				zipobj.extractall(dir_place)
if teste == False: dezipar_jogos()
#%%
### RESOLVER O WINDOWS: SITE DE MERDA Q EU ACHEI 
def dezipar_windows():	
	with ZipFile('win31.zip', 'r') as zipobj:
		# print(zipobj.namelist())
		for file in zipobj.namelist():			
			if file.startswith('WINDOWS'):
				zipobj.extract(file, '')
dezipar_windows()

