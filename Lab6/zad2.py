# Zadanie 2. Dla macierzy losowej 6x4 (N(0,1)) znajdz: srednia kazdej kolumny, indeksy min/max w kazdej kolumnie
import numpy as np

gen = np.random.default_rng(10)
mac = gen.normal(0, 1, (6, 4))

print(mac)
print(mac.mean(axis=0))
print(np.argmax(mac, axis=0))
print(np.argmin(mac, axis=0))
