set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

#union
set_c = set_a.union(set_b)

print('\nUnión\n',set_c)
#el operador | funciona como el .union
print('\nUnión con operador\n',set_a | set_b)

#interseccion
set_c = set_a.intersection(set_b)
print('\nIntersección\n',set_c)
print('\nIntersección con operador\n',set_a & set_b)

#Diferencia

set_c = set_a.difference(set_b)
print('\nDiferencia\n',set_c)
print('\nDiferencia con operador\n',set_a - set_b)

#simetric diference 
set_c = set_a.symmetric_difference(set_b)
print('\nSymetric Difference\n',set_c)
print('\nSymetric Difference con operador \n',set_a ^ set_b)
