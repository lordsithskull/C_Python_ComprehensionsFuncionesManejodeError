set_countries = {'col', 'mex', 'bol'}
size = len(set_countries)
print(size)

print('mex' in set_countries)
print('eu' in set_countries)

#add PERMITE AGREGAR UN ELEMENTO, SI YA SE ENCUENTRA NO LO AGREGARÁ
set_countries.add('pe')
print(set_countries)
set_countries.add('pe')
print('\n',set_countries)

#Update
set_countries.update({'ar', 'ecua', 'pe'})
print('\n',set_countries)

#remove
set_countries.remove('col')
print('\n',set_countries)
#si queremos hacer una pequeña comprobacion podemos usar discard en vez de remove
set_countries.discard('per')
print('\n',set_countries)

#metodo para limpiar el conjunto
set_countries.clear()
print('\n',set_countries)
print(len(set_countries))