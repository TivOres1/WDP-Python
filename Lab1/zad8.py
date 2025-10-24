# Zad 8

import math

a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))

if a == 0:
    if b == 0:
        print("To nie jest rownanie: brak zmiennej x.")
    else:
        x = -c / b
        print("Rownanie liniowe, rozwiazanie:", x)
else:
    delta = b**2 - 4*a*c

    if delta < 0:
        print("Brak rozwiazan rzeczywistych.")
    elif delta == 0:
        x = -b / (2*a)
        print("Jedno rozwiazanie:", x)
    else:
        x1 = (-b - math.sqrt(delta)) / (2*a)
        x2 = (-b + math.sqrt(delta)) / (2*a)
        print("Dwa rozwiazania: x1:", x1, ", x2:", x2)
