# Zadanie 6.
# Odpowiedz na pytania i krótko uzasadnij odpowiedź:
# WSTĘP DO PROGRAMOWANIA – LAB. 5
# 1. Co się stanie? Czy kod się wykona, czy wystąpi błąd? Jeśli błąd, podaj jego typ i powód.

# def t(x, *, y, z=0):
#     return x + y + z

# val= t(1, 2, z=3)


# 2. Wyjaśnij co dokładnie zwróci y oraz jak Python rozdzielił argumenty.

f = lambda a, /, *args, b=0: (a, sum(args) + b)
y = f(3, 4, 5, b=2)

print(y)