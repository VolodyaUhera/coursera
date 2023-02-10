""" sample_dict = {1: 'Coffe', 2: 'Tea', 3: 'Juice'}

print(sample_dict)

sample_dict[2] = 'Mint Tea'

print(sample_dict[1])

del sample_dict[3]

print(sample_dict)

print(type(sample_dict))

for keys, x in sample_dict.items():
    print(str(keys) + " : " + x)
     """

tel = {'jeck': 4098, 'sape': 4139}

tel['guido'] = 4127

squares = {x: x**2 for x in range(5)}

print(squares)
print(squares[0])

tel['mody'] = 3344

print(tel)

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k,v in knights.items():
    print(k, v)
    
for k,v in enumerate(knights.items()):
    print(k, v)


