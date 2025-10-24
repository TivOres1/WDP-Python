# Zad 9

a = float(input("Podaj pierwsza liczbe: "))
b = float(input("Podaj druga liczbe: "))

suma = a + b
roznica = a - b
iloczyn = a * b

if b != 0:
    iloraz = a / b
else:
    iloraz = "Nie mozna dzielic przez zero"

potega = a ** b

print("Suma:", suma)
print("Roznica:", roznica)
print("Iloczyn:", iloczyn)
print("Iloraz:", iloraz)
print("Potega:", potega)
