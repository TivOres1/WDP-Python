# Zad 6.
# Podana jest poniższa krotka owoce:
# owoce = ('jabłko', 'banan', 'gruszka', 'banan', 'banan', 'malina')
# Stwórz program, który wykorzystuje odpowiednią metodę do zliczenia wystąpień elementu 'banan' w
# krotce. 

owoce = ('jabłko', 'banan', 'gruszka', 'banan', 'banan', 'malina')
i = 0
for element in owoce: 
    if element == "banan":
        i+=1

print(i)


