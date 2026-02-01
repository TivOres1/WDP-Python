# Zadanie 1. Stworz tablice 5x5 (wartosci od 0 do 24) i wyciagnij obramowanie
import numpy as np

tab = np.arange(25).reshape(5, 5)

print(tab[0,:])
print(tab[-1,:])
print(tab[:,0])
print(tab[:,-1])
