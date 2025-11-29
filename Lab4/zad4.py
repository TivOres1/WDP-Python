# Zad. 4 dodatkowe
# Napisz program, który wczyta od użytkownika zdanie. Wypisz z niego wszystkie litery w kolejności
# alfabetycznej, a następnie wypisz te litery, których to zdanie nie zawiera.


zdanie = "będę antyk dede aafs"
slowa = zdanie.split()
posortowane_slowa = sorted(slowa)
nowe_zdanie = " ".join(posortowane_slowa)

print(nowe_zdanie)