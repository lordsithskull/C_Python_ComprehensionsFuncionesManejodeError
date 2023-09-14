def find_volume(lenght = 1 , width = 1, depth = 1):
  return lenght * width * depth, "resultado"


result = find_volume(10, 2,3)

print(result)
print(10 * '*')

#solo asignamos el valor de width
result = find_volume(width = 10)

print(result[0])
print(10 * '*')

#
result, text = find_volume(width = 10)

print(result)
print(text)
