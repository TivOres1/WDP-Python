# Zad. 2.
# Napisz program, który wydrukuje do konsoli 10 pierwszych liczb pierwszych rozdzielonych
# przecinkiem tak jak pokazano poniżej.
# Pamiętaj, że liczba pierwsza - to taka liczba naturalna, która ma dokładnie dwa dzielniki naturalne:
# jedynkę i samą siebie.
# W rozwiązaniu użyj pętli while oraz instrukcji break
# Oczekiwany wynik:
# 2,3,5,7,11,13,17,19,23,29

listaLiczb = [] 
i = 2

while len(listaLiczb) < 10:
    jestPierwsza = True

    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            jestPierwsza = False
            break

    if jestPierwsza:
        listaLiczb.append(+i)

    i += 1

print(", ".join(map(str, listaLiczb)))


