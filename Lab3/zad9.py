# Zad. 9
# Napisz programy, które:
# • Wczyta (zmienną) imię oraz wyświetli tekst „Witaj” oraz wczytane imię.
# • Wczyta (zmienną) wiek oraz wyświetli tekst „Twój wiek to: ” oraz wczytany
# wiek.
# • Wczyta (zmienne) imię i nazwisko i wyświetli inicjały.
# • Wczyta łańcuch i wyświetli go pięć razy.
# • Wczyta dwa łańcuchy, a w trzecim łańcuchu zapamięta połączone te dwa
# łańcuchy.
# • Wczyta dwa łańcuchy, a w trzecim łańcuchu zapamięta pierwszą połowę

imie = str(input("Podaj imie: "))
wiek = int(input("Podaj wiek: "))

print(f"Witaj {imie}. Twoj wiek to: {wiek}")

imieSec = str(input("Podaj imie: "))
nazwisko = str(input("Podaj nazwisko: "))
print(f"Twoje inicjaly: {imieSec[0]}.{nazwisko[0]}.")

lancuch = input("Podaj lancuch: ")
print(lancuch * 5)

lancuch1 = input("Podaj pierwszy lancuch: ")
lancuch2 = input("Podaj drugi lancuch: ")
polaczony = lancuch1 + lancuch2
print("Polaczony lancuch:", polaczony)

tekst = input("Podaj lancuch: ")
polowa = len(tekst) // 2
polowka = tekst[:polowa]
print("Pierwsza polowa lancucha:", polowka)
