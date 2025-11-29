# Zad. 2
# Stwórz listę z imionami 4 osób.
# a. Posortuj ją alfabetycznie i wyświetl,
# b. Dodaj na końcu dwie osoby i pobierz ostatnią z nich poleceniem pop().
# c. Na pozycji 3 dodaj jeszcze jedną osobę.
# d. Odwróć kolejność na liście i zduplikuj ją.

imiona = ["John", "Test", "Barbara", "Andrzej"]

print(sorted(imiona))

imiona.append("Muhamed")
imiona.append("Jacek")

print(imiona)
print(imiona.pop())

imiona.insert(2,"Imie")

print(imiona)

imionaSec = imiona[::-1]
print(imionaSec)

