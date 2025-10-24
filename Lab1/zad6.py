# Zad 6

# bez modyf.

droga = float(input("Podaj droge: "))
spalanie = float(input("Podaj spalanie na 100km: "))
cenaPal = float(6.5)
koszty = round(((droga/100) * spalanie) * cenaPal, 2)
print("Koszt podrozy to: "+str(koszty)+" zl.")

# z modyf

import random

# a)
drogaRand = random.randint(0, 2000)
kosztyRand = round(((drogaRand/100) * spalanie) * cenaPal, 2)

# b)
print(f"Rand droga to: {drogaRand}, Koszt podrozy to: {kosztyRand} zl")