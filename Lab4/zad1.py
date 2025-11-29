# Zad. 1
# Utwórz listę: Moja_lista=[1, 17, 3, 5, 3, 4, 86, 90, 2, 21], przetestuj działanie wszystkich
# zaprezentowanych operacji na listach, a ich wynik wyświetl w konsoli.


# lista[0]
# lista[-1]
# len(lista)
# max(lista)
# min(lista)
# sum(lista)
# sorted(lista)
# lista.append(6)
# lista.insert(i,5)
# lista.pop()
# lista.reverse()
# lista = lista1 + lista2
# listaM = lista1*5
# lista[ :n]
# lista[m: ]
# lista[m:n:k]
# lista[::-1]

Moja_lista=[1, 17, 3, 5, 3, 4, 86, 90, 2, 21]

print(Moja_lista)
print(Moja_lista[0])
print(Moja_lista[-1])

print(len(Moja_lista))
print(max(Moja_lista))
print(min(Moja_lista))
print(sum(Moja_lista))
print(sorted(Moja_lista))

Moja_lista.append(6)
print(Moja_lista)

Moja_lista.insert(2, 5)
print(Moja_lista)

print(Moja_lista.pop())

Moja_lista.reverse()
print(Moja_lista)

test1 = [1, 10, 20, 5, 9]
test2 = [1, 10, 20, 5, 9]

test = test1 + test2
print(test)

testM = test1*5
print(testM)

print(testM[:3])
print(testM[2: ])
print(testM[2:2:5])
print(testM[::-1])

