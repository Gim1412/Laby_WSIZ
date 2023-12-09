print("Program1")

print("Pole prostokąta = x*y")
print("Obwód prostokąta = 2x+2y")

x=int(input("podaj długość boku x:"))
print("x =", x)
y=int(input("podaj długość boku y:"))
print("y =", y)

print("Pole prostokąta x*y = ",x*y)

print("Obwód prostokąta 2x + 2y = ",2*x+2*y)


print("Program2")

print("Koszty Podróży")

import random
los = random.randint(1, 100000)


print("Długość podróży : ", los, "km")

y = int(input("podaj średnie spalanie (w litrach na 100 km) :"))
print("Średnie spalanie :", y, "l/100km")

zużycie = round(y/100*los, 2)

koszty = round(y/100*los*6.5, 2)

zdanie = f'Przewidywane zyżycie paliwa : {zużycie} l"  Przewidywany koszt podróży : {koszty} zł'

print(zdanie)




