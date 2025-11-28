# Zad. 7 dodatkowe
# A)
# Grupa laboratoryjna składa się z n studentów (wartość n podaje użytkownik). Wprowadzamy liczbę
# punktów dla każdego studenta.
# Napisz program, który obliczy średnią liczbę punktów w grupie z wykorzystaniem pętli while.
# Zastosuj instrukcje continue w programie tak, aby po podaniu liczby punktów spoza przedziału 0 –
# 100 pomijać dalsze wykonywanie pętli. Sprawdź działanie programu.
# B)
# Następnie zmień pętlę na nieskończoną, czyli taką której warunek zawsze jest prawdziwy. Zakończ
# działanie pętli przy użyciu instrukcji break.
# Obie wersje zadnia proszę zamieścić w sprawozdaniu.

n = int(input("Podaj liczbe studentow: "))
i = 0
suma = 0

while i < n:
    pkt = float(input("Podaj liczbe punktow: "))
    if pkt < 0 or pkt > 100:
        continue
    suma += pkt
    i += 1

srednia = suma / n
print("Srednia punktow:", srednia)


m = int(input("Podaj liczbe studentow: "))
j = 0
sumaSec = 0

while True:
    pktSec = float(input("Podaj liczbe punktow: "))
    if pktSec < 0 or pktSec > 100:
        continue
    sumaSec += pktSec
    j += 1
    if j == m:
        break

sredniaSec = sumaSec / m
print("Srednia punktow:", sredniaSec)

