# Podana jest poniższa zmienna przechowująca ciąg znaków - hasło:
# Hasło = 'pk47!jy0893'
# Sprawdź, czy podane hasło ma wymaganą długość 11 znaków oraz zwiera znak specjalny '!'. Jeżeli
# tak, wydrukuj do konsoli „Hasło jest poprawne”, w przeciwnym razie „Hasło jest nie poprawne”.

haslo = 'pk47!jy0893'

print(len(haslo))

if len(haslo) >= 11 and '!' in haslo:
    print("Haslo poprawne")
else: 
    print("Haslo nie poprawne")