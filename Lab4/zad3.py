# Zad. 3
# Napisz program, który:
# a. Wczyta (zmienną) imię oraz wyświetli tekst „Witaj” oraz wczytane imię.
# b. Wczyta (zmienną) wiek oraz wyświetli tekst „Twój wiek to:” oraz wczytany wiek.
# c. Wczyta (zmienne) imię i nazwisko i wyświetli inicjały.
# d. Wczyta łańcuch i wyświetli go pięć razy.
# e. Wczyta dwa łańcuchy, a w trzecim łańcuchu zapamięta połączone te dwa łańcuchy.
# f. Wczyta dwa łańcuchy, a w trzecim łańcuchu zapamięta pierwszą połowę pierwszego i drugą połowę
# drugiego.

imie=str(input("Podaj imie: "))
print(f"Witaj {imie}")

wiek=int(input("Podaj wiek: "))
print(f"Twoj wiek to {wiek}")

imieSec = str(input("Podaj imie: "))
nazwisko = str(input("Podaj nazwisko: "))
print(f"Twoje inicjaly: {imieSec[0]}.{nazwisko[0]}.")

lista = []
for i in range(0, 5):
    tekst = str(input("Podaj test: "))
    lista.append(tekst)

print(lista*5)

lista2 = []
for i in range(0, 4):
    tekst2 = str(input("Podaj test: "))
    lista2.append(tekst2)

lista3 = []
for i in range(0, 4):
    tekst3 = str(input("Podaj test: "))
    lista3.append(tekst3)    

listaSum = lista2 + lista3
print(listaSum)

test = lista2[:len(lista2) // 2] + lista3[len(lista3) // 2 :]

print(test)




