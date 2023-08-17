#numbers sera una lista de elementos en un rango

numbers = []
for element in range(1, 11):
  numbers.append(element * 2)

print(numbers)

#esta es la misma sentencia que las sentencias de arriba, pero todo en una sola línea
numbers_v2 = [element * 2 for element in range(1,11)]
print(numbers_v2)
'''
    Otro ejemplo
'''
print('\n')
numbers_3 = []
for i in range(1, 11):
  if i % 2 == 0:
    numbers_3.append(i * 2)

print(numbers_3)

numbers_v4 = [i * 2 for i in range(1,11) if i %2 == 0  ]

print(numbers_v4)