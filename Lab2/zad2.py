# Napisz program porządkowania trzech liczb x, y i z. Od najmniejszej do największej, bez użycia
# wbudowanych funkcji

x=2
y=5
z=3

if x >= y and x >=z:
    if y >= z:
        print(x,y,z)
    else:
        print(x,z,y)
elif y >= x and y >=z:
    if x >= z:
        print(y,x,z)
    else:
        print(y,z,x)
elif z >= x and z >=y:
    if x >= y:
        print(z,y,z)
    else:
        print(z,x,y)