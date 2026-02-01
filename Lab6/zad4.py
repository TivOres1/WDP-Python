# Zadanie 4. Utworz tablice A=(2,3) B=(3,2). Oblicz iloczyn skalarny, zmien rozmiar B na (3,3) i sprawdz mnozenie
import numpy as np

A = np.arange(1, 7).reshape(2, 3)
B = np.arange(1, 7).reshape(3, 2)

print(A @ B)
print(B @ A)

B = np.ones((3, 3))

try:
    print(A @ B)
    print(B @ A)
except ValueError as e:
    print(e)
