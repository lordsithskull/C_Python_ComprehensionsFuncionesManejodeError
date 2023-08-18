#dictionary comprensions parte 2
import random

countries = {'mex', 'col', 'bol', 'pe'}

population_v2 = {country: random.randint(1, 30) for country in countries}
print(population_v2)

result = {
    country: population
    for (country, population) in population_v2.items() if population > 20
}
print(result)
print("\n")

text = 'Hola soy Miguel'
unique = {c: c.upper() for c in text if c in 'aeiou' }
print(unique)