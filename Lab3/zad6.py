# Zad. 6
# Napisz pętlę nieskończoną, w której użytkownik podaje liczby całkowite. W przypadku liczby ujemnej,
# następuję wyjście z pętli.

jestUjemna = False

while jestUjemna == False:
    liczba=int(input("Podaj liczbe: "))
    if(liczba < 0):
        jestUjemna = True
        print("Podales liczbe ujemna!")