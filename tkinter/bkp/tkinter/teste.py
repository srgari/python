
d = {'241600':['Rogue Legacy','metroidvania'],
'200900':['Cave Story+','metroidvania'],
'678950':['Dragon Ball Fighterz'],
'363440':['Mega Man Legacy Collection'],
'743890':['Mega Man X Legacy Collection'],
'263980':['Out There Somewhere'],
'553640':['Icey'],
'310950':['Street Fighter V'],
'379720':['Doom 2016'],
'730':['Counter Strike GO'],
'360940':['Mean Greens Plastic Warfare'],
'219150':['Hotline Miami'],
'212680':['Faster Than Light'],
'367520':['Hollow Knight','metroidvania'],
'70':['Half Life'],
'2290':['Final Doom'],}

nomes = ([x[0] for x in (d.values())])

print({x:y for x,y in zip(nomes, d.keys())})