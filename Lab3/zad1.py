# Zad. 1
# Napisz program, który będzie kontrolować zużycie paliwa w samolocie. Przed rozpoczęciem każdej
# jednostki czasu wydrukuj do konsoli informację o pozostałych jednostkach paliwa. Gdy paliwo
# zostanie wyczerpane, wydrukuj do konsoli informacje 'Koniec lotu.'.

# Masz do dyspozycji następujące dane.:
# • ilość paliwa w samolocie w litrach
# • ilość paliwa zużywanego na sekundę w litrach
# • czas lotu w sekunadach

# Wartości początkowe:
# • paliwo = 100
# • paliwo_zużyte_na_s = 10
# • czas = 0

paliwo = int(100)
zuzPaliwa = int(10)
czas = paliwo / zuzPaliwa
i = int(0)

while i < czas:
    print("Pozostalo paliwa: "+str(paliwo)+"\n")
    paliwo = paliwo - zuzPaliwa
    i = i + 1

print("Koniec lotu")