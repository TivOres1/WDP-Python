# Zad. 5
# Napisz kod, który generuje listę liczb zmniejszających się o 4, zaczynając od 80 i kończąc w 0.

listaLiczb = []
i = 80

while i != 0:
    i = i - 4
    listaLiczb.append(i)

print(str(listaLiczb))