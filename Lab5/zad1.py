# Zadanie 1.
# Napisz funkcję, która oblicza pierwiastki funkcji kwadratowej. Funkcja przyjmuje argumenty a,b,c,
# które są współczynnikami funkcji kwadratowej. Dla a=0, napisz wyjątek, gdy funkcja nie jest
# kwadratowa. Skorzystaj z biblioteki math. Napisz dokumentację tej funkcji, kiedy jest co obliczane itp.

import math

def quadratic_roots(a, b, c):
    if a == 0:
        raise ValueError("not quadratic")
    delta = b*b - 4*a*c
    if delta < 0:
        return ()
    if delta == 0:
        return (-b / (2*a),)
    sqrt_delta = math.sqrt(delta)
    x1 = (-b - sqrt_delta) / (2*a)
    x2 = (-b + sqrt_delta) / (2*a)
    return (x1, x2)

print(quadratic_roots(1, -5, 6))