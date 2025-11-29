# Zad 9.
# Stwórz listę zakupów jako słownik (artykuł : kwota). Wyświetl go i podsumuj wydatki.

zakupy = {
    "chleb" : 2, 
    "woda" : 1, 
    "mieso" : 10, 
    "maslo" : 5, 
    "mleko" : 3, 
}

print(zakupy)

wydatki = 0

for i in zakupy.values():
    wydatki = wydatki + i

print(wydatki)