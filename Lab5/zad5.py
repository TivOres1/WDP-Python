# Zadanie 5.
# Napisz funkcję zmieniającą miejscami dwa elementy listy wraz z obsługą wyjątków.
# Wymagania
# 1. Funkcja przyjmuje listę oraz indeksy.
# 2. Działa in-place (modyfikacja istniejącej listy)
# 3. Obsługuje ujemne indeksy
# 4. Wyrzuca:
# a. ValueError, gdy lista jest pusta
# b. TypeError, gdy argumenty mają niewłaściwe typy
# c. IndexError, gdy indeksy wychodzą poza zakres
# 5. (Dla chętnych - napisanie testów przy pomocy biblioteki pytest)

def swap_elements(lst, i, j):
    if not isinstance(lst, list) or not isinstance(i, int) or not isinstance(j, int):
        raise TypeError("invalid type")
    if len(lst) == 0:
        raise ValueError("empty list")
    if i < -len(lst) or i >= len(lst) or j < -len(lst) or j >= len(lst):
        raise IndexError("index out of range")
    lst[i], lst[j] = lst[j], lst[i]
    return lst

lst = [10, 20, 30, 40]
swap_elements(lst, 1, -1)
print(lst)