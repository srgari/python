d = {'241600':'Rogue Legacy',
'200900':'Cave Story+',
'678950':'Dragon Ball Fighterz',
'363440':'Mega Man Legacy Collection',
'743890':'Mega Man X Legacy Collection',
'263980':'Out There Somewhere',
'553640':'Icey',
'310950': 'Street Fighter V'}

keys = list(d.keys())
values = list(d.values())


d2 = {x:y for x,y in zip(values,keys)}

print(d2)