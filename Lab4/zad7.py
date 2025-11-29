# Zad 7.
# Posortu krotke moja_krotka= (10, 2, 6, 6, 9, 13, 0,1), operacji tej dokonaj posługując się pomocniczo
# listą

lista = []
moja_krotka= (10, 2, 6, 6, 9, 13, 0,1)

i = 0
for element in moja_krotka: 
    lista.append(element)

print(sorted(lista))