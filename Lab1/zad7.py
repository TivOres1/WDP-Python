# Zad 7

a = float(input("Podaj a: "))
b = float(input("Podaj b: "))

if a == 0:
    if b == 0:
        print("Rownanie ma nieskonczenie wiele rozwiazan.")
    else:
        print("Rownanie sprzeczne – brak rozwiazan.")
else:
    x = -b / a
    print("Rozwiazanie: x: ", x)