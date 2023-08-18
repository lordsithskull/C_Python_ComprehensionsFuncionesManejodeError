#Playgrounds: Elimina elementos duplicados usando conjuntos
countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

new_set = set()
#solución 👇
new_set = countries.union(northAm, centralAm, southAm)

print(new_set)