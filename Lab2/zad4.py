# Jesteś menagerem drużyny piłkarskiej i chcesz obliczyć łączny wynik drużyny na podstawie liczby
# strzelonych przez nią bramek i ewentualnie zdobytych dodatkowych punktów. Napisz program,
# który dokona stosownych kalkulacji po wprowadzeniu liczby goli zdobytych przez drużynę.
# Utworzone są dwie zmienne gol i bonus, gdzie gol to liczba całkowita reprezentująca liczbę
# bramek zdobytych przez drużynę, a bonus to liczba całkowita reprezentująca wszelkie możliwe
# punkty bonusowe dla drużyny.
# Następnie użyj instrukcji warunkowej do obliczenia całkowitego wyniku zespołu zgodnie z
# następującymi zasadami:
# - każda zdobyta bramka to 10 punktów,
# - jeśli drużyna zdobędzie więcej niż 5 bramek, zdobywa dodatkowe 5 punktów bonusowych,
# - jeśli drużyna zdobędzie więcej niż 10 bramek, zdobywa dodatkowe 10 punktów bonusowych
# a) Po zdobyciu 5 goli drużyna otrzymuje 5 punktów bonusowych. Jeśli drużyna zdobędzie więcej
# niż 10 goli, to otrzyma za nie 10 punktów bonusowych dodatkowo
# Oblicz całkowity wynik drużyny, dodając punkty zdobyte ze zdobytych bramek i wszelkie
# stosowne punkty bonusowe. Wynik wydrukuj do konsoli.
# b) Punkty bonusowe po przekroczeniu 5 i 10 punktów są sumowane, tzn. po przekroczeniu więcej
# niż 10 bramek drużyna zdobywa obydwa bonusy.
# Oblicz całkowity wynik drużyny, dodając punkty zdobyte ze zdobytych bramek i wszelkie
# stosowne punkty bonusowe. Wynik wydrukuj do konsoli.

bramki=int(input("Podaj bramki: "))

pkt = bramki * 10

if bramki > 10:
    pkt = pkt + 15
    print(f"Pkt z oboma bonusami bo 10 bramek lub wiecej: {pkt}")
elif bramki > 5 and bramki < 10:
    pkt = pkt + 5
    print(f"Pkt z bonusami bo bramek wiecej niz 5 ale mniej niz 10: {pkt}")
else:
    print(f"Pkt bez bonusow: {pkt}")

bramkiSec=int(input("Podaj bramki 2: "))

pktSec = bramkiSec * 10

if bramkiSec > 10:
    pktSec = pktSec + 10
    print(f"Pkt z oboma bonusami bo 10 bramek lub wiecej: {pktSec}")
elif bramkiSec > 5 and bramkiSec < 10:
    pktSec = pktSec + 5
    print(f"Pkt z bonusami bo bramek wiecej niz 5 ale mniej niz 10: {pktSec}")
else:
    print(f"Pkt bez bonusow: {pktSec}")

