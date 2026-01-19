# Zadanie 4.
# Napisz funkcję sum_digits(n), która oblicza sumę cyfr liczby rekurencyjnie. Napisz dokumentacje tej
# funkcji, która opisywać będzie jej działanie.

def sum_digits(n):
    n = abs(n)
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)


print(sum_digits(12345))
print(sum_digits(-908))