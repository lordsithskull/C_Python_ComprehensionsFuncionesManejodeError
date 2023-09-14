price = 100 #scope global
result = 300

def increment():
  #scope local
  price = 200
  result = price + 10
  print(result)
  return result

print(price)
price_2 = increment()
print(price_2)
print(result)