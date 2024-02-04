# LABORATORIUM 5

# 1 a)Numerek

import random

numerek = random.randint(0, 1000)

print(f"Szczęśliwy numerek: {numerek}")

# 1 b) Szczęśliwy rocznik

roczniki = list(range(1995, 2003))
szczesliwy_rocznik = random.choice(roczniki)

print(roczniki)
print("Szczęśliwy rocznik:", szczesliwy_rocznik)

# 1 c) Duży lotek

beben = list(range(1, 50))

wynik = random.sample(beben, 6)

print("Wyniki losowania:", wynik)

# 2 Pierwiastki

import math

wynik1 = math.sqrt(81)
print("√81 =", wynik1)

wynik2 = math.sqrt(810)
print("√810 =", wynik2)

wynik3 = math.sqrt(2) + math.sqrt(3) + math.sqrt(6)
print("√2 + √3 + √6 =", wynik3)

wynik4 = 3 * math.pow(125, 1 / 3)
print("3√125 =", wynik4)

# 3  Sekundnik

import time


def sekundy(czas):
    while czas > 0:
        print(f"{czas} ")
        time.sleep(1)
        czas -= 1

    print("0")


czas = int(input("Podaj liczbę sekund:"))
sekundy(czas)

# 4  Dni do kolokwium
from datetime import datetime, timedelta

data_lab = datetime(2024, 1, 14)

data_kolokwium = datetime(2024, 2, 11)

aktualna_data = datetime.now()

dni_od_labo= (aktualna_data - data_lab).days

czas_do_kolokwium = (data_kolokwium - aktualna_data)

print(f"Od ostatnich laboratoriów minęło: {dni_od_labo} dni .")
print(f"Dni do kolokwium: {czas_do_kolokwium.days} dni")


#  5 Słowa kluczowe

import keyword

slowa= ["for", "print", "break", "done", "bad"]

for slowo in slowa:
    if keyword.iskeyword(slowo):
        print(f"{slowo} jest słowem kluczowym")
    else:
        print(f"{slowo} nie jest słowem kluczowym")


# 6  Nazwy funkcji

print("Funkcje math:")
print(dir(math))

print("Funkcje keyword:")
print(dir(keyword))

print("Funkcje w module tuple:")
print(dir(tuple))

# 7 Średnia geometryczna


