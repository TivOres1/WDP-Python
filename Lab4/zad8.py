# Zad 8.
# Załóżmy, że pracujesz nad systemem wojskowym dotyczącym planowania operacji wojskowych.
# Podana jest poniższa krotka:
# stopnie = (
#  "Szeregowy",
#  "Kapral",
#  "Sierżant",
#  "Porucznik",
#  "Kapitan",
#  "Major",
#  "Pułkownik",
# )
# Wykonaj poniższe kroki:
# - wyznacz liczbę wszystkich stopni wojskowych i przypisz do zmiennej ilość_stopnii,
# - znajdź indeks krotki dla elementu "Major" i przypisz do zmiennej Major_index,
# - sprawdź, czy wartość "Pułkownik" znajduje się w krotce stopnie i przypisz do zmiennej
# Pułkownik_wstepowanie.
# W wydrukuj otrzymane zmienne do konsoli w podanej kolejności.

stopnie = (
 "Szeregowy",
 "Kapral",
 "Sierżant",
 "Porucznik",
 "Kapitan",
 "Major",
 "Pułkownik",
)

i = 0
for element in stopnie: 
    i+=1

print(f"Liczba stopni: {i}")

Major_index = 0
j = 0
for element in stopnie: 
    if element == "Major":
        Major_index = j
        break
    else: 
        j+=1

print(Major_index)


Pułkownik_wstepowanie  = ""
for element in stopnie: 
    if element == "Pułkownik":
        Pułkownik_wstepowanie = element

print(Pułkownik_wstepowanie)