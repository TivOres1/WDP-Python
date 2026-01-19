# Zadanie 3.
# Napisz funkcję, która zwraca listę tylko z liczbami parzystymi. Funkcja przyjmuje dowolną ilość
# argumentów. Wykorzystaj funkcję filter oraz lambda.

def even_numbers(*args):
    return list(filter(lambda x: isinstance(x, int) and x % 2 == 0, args))

print(even_numbers(1, 2, 3, 4, 5, 6, 7, 8))