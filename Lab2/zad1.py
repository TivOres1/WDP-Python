# Napisz prosty program, który na podstawie podanej przez Studenta liczby zdobytych punktów,
# poinformuje go o rezultacie egzaminu.
# Każdy Student, który zdobył powyżej 80 punktów zalicza egzamin w terminie 0
# Studenci którzy otrzymali liczbę punków z przedziału 50-80, mogą poprawić jego wynik.
# Studenci, którzy zdobyli poniżej 50 punktów, muszą go poprawić.

pkt=int(input("Podaj liczbe pkt: "))

if pkt >= 80:
    print("Zaliczyles egzamin")
elif pkt >= 50 and pkt < 80:
    print("Zaliczyles ale mozesz poprawic")
else:
    print("Musisz poprawic")
