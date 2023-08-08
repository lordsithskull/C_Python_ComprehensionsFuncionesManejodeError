#definir un conjunto estableciendo la palabra set al inicio del conjunto
set_countries = {'México', 'Colombia', 'Bolivia'}
print(set_countries)
print(type(set_countries))
#los conjuntos no muestran elementos repetidos
set_numbers = {1, 2, 2, 443, 23}
print(set_numbers)

set_types = {1, 'hola', False, 12.12}
print(set_types)
print(type(set_types))

set_from_string = set('hola')
print(set_from_string)

set_from_tuples = set(('abc', 'cbv', 'asd'))
print(set_from_tuples)

#se puede transformar a lista o diccionario
numbers = [1, 2, 1, 3, 1, 3, 4, 5, 6]
set_numbers = set(numbers)
print(set_numbers)
unique_numbers = list(set_numbers)
print(unique_numbers)
print(type(unique_numbers))
