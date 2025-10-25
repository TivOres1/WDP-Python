# zad. 5
# a)
# Odczytaj podany plik notwania_gieldowe.txt zawierający dane dotyczące notowań kilku spółek.
# Wydrukuj każdą linię do konsoli.
# b)
# Dopisz do pliku notwania_gieldowe.txt, w kolejnej linii dane dotyczące nowej spółki: ALR, 113.
# Wydrukuj każdą linię ponownie do konsoli.

with open("./WDP-Python/Lab2/notowania_gieldowe.txt", "r") as plik:
    print(plik.readlines())

with open("./WDP-Python/Lab2/notowania_gieldowe.txt", "a") as plik:
    plik.writelines("\nALR, 113")

with open("./WDP-Python/Lab2/notowania_gieldowe.txt", "r") as plik:
    print(plik.readlines())



    