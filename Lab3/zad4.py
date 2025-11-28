# Zad 4. dodatkowe
# Zamówiłeś w restauracji z grupą x przyjaciół, n potraw (liczbę zamówionych dań i liczbę gości, za
# każdym razem wskazuje użytkownik), następnie dla każdej potrawy podajesz jej cenę.
# Korzystając z pętli while napisz program, który pozwoli obliczyć średnią cenę zamówionej potrawy.
# Podziel sprawiedliwe rachunek miedzy wszystkich gości. 

x = int(input("Podaj liczbe gosci: "))
n = int(input("Podaj liczbe potraw: "))

suma = 0
i = 1

while i <= n:
    cena = float(input(f"Podaj cene potrawy nr {i}: "))
    suma += cena
    i += 1

srednia = suma / n
na_osobe = suma / x

print("Srednia cena potrawy:", srednia)
print("Kwota do zaplaty na jedna osobe:", na_osobe)