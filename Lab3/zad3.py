# Zad. 3.
# Mając podana listę ulic w danej dzielnicy i wiedząc, że na każdej ulicy znajduje się 5 bloków
# mieszkalnych, a w każdym z nich jest 10 lokali, wypisz listę wszystkich adresów w dzielnicy.
# Lista ulic w dzielnicy:
# • Jagodowa,
# • Lipowa,
# • Kwiatowa,
# • Kasztanowa,
# • Polna

listaUlic = ["Jagodowa", "Lipowa", "Kwiatowa", "Kasztanowa", "Polna"]
i = 0
for i in range(5):
    for j in range(5):
        if j == 0: 
            j = "A"
        elif j == 1:
            j = "B"
        elif j == 1:
            j = "C"
        elif j == 1:
            j = "D"
        else: 
            j = "E"

        for k in range(1, 11):
            print("ul."+str(listaUlic[i])+" blok: " + str(j) +" mieszkanie: "+str(k))
    