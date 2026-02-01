# Zadanie 3. Utworz tablice a=[1,2,3,4], b=[10,20,30,40], pomnoz element po elemencie i wyznacz iloczyn skalarny
import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([10, 20, 30, 40])

print(arr1 * arr2)
print(arr1 @ arr2)
