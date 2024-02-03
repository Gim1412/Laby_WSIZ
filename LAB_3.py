# Laboratorium 3

# Zadanie 1.1

tekst = "Rzeszów jest piękny"

print(tekst[0])
print(tekst[6], tekst[9], tekst[12], tekst[1])

# Zadanie 1.2

tekst = "Python jest super"

print(tekst[0])
print(tekst[-1])
print(tekst[:: 2])
print(tekst[1: -1: 3])
print(tekst[9:])
print(tekst[::-1])

# Zadanie dodatkowe

imie = input("Podaj swoje imię: ")
print("Witaj", imie)
wiek = input("Podaj swój wiek: ")
print("Twój wiek to: ", wiek, "lat(a)")

imie = input("Podaj swoje imię:")
nazwisko = input("Podaj swoje nazwisko: ")
print(imie[0], nazwisko[0])

tekst = input("Wpisz dowolny tekst:")

print(tekst * 5)

tekst = input("Wpisz dowolny tekst:")
tekst2 = input("Wpisz drugi dowolny tekst:")
print(tekst + tekst2)

tekst = input("Wpisz dowolny tekst:")
tekst2 = input("Wpisz drugi dowolny tekst:")

x1 = len(tekst)
x2 = len(tekst2)

polowa1 = x1 // 2
polowa2 = x2 // 2
trzeci = tekst[:polowa1] + tekst2[polowa2:]
print("Trzeci łańcuch:", trzeci)

# Lista

lista = ["Ewa", "Adam", "Ola", "Ula"]
lista.sort()
print(lista)
lista.append("Ala")
lista.append("Iga")
print(lista)
lista.pop()
print(lista)
lista.insert(2, "Andrzej")
lista.reverse()
print(lista)
lista2 = lista * 2
print(lista2)

# Część druga

# Zadanie 2.1

import random

x = int(input("Liczba ciągów: "))
n = int(input("Liczba elementów: "))

lista_ciagow = []
for i in range(n):
    dlugosc = random.randint(1, x)

    ciag = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(dlugosc))

    lista_ciagow.append(ciag)

print("Utworzone ciągi:", lista_ciagow)

lista_ciagow2 = tuple(lista_ciagow)

# ilość znaków
ilosc_znakow = 0
for ciag in lista_ciagow2:
    ilosc_znakow += len(ciag)
print("Ilość znaków:", ilosc_znakow)

# Litera k

ilosc_k = 0

for ciag in lista_ciagow2:
    ilosc_k += ciag.count('k')

print("Liczba wystąpień litery k:", ilosc_k)

# Wystąpienia "kt"

ilosc_kt = 0
for ciag in lista_ciagow2:
    ilosc_kt += ciag.count('kt')
print("Ilość wystąpień kt", ilosc_kt)

# Ciągi dłuższe od s
s = int(input("Podaj liczbę s:"))
dlugie = 0
for ciag in lista_ciagow2:
    if len(ciag) > s:
        dlugie += 1
print("Ilość ciągów dłuższych od s:", dlugie)

# Zadanie 2.1

lista_zakupow = {"spodnie": 100, "buty": 200, "koszula": 300, "kurtka": 50}

print("Lista zakupów:", lista_zakupow)

suma_wydatkow = sum(lista_zakupow.values())
print(f"Suma wydatków: {suma_wydatkow} PLN")

#  Rachunki za prąd

rachunki = {'maj': 200, 'czerwiec': 230, 'lipiec': 300, 'sierpień': 330, 'marzec': 270}
print(rachunki)
kwoty_rachunkow = list(rachunki.values())

#rachunki a

maksymalna_kwota = max(kwoty_rachunkow)
minimalna_kwota = min(kwoty_rachunkow)
suma_kwot = sum(kwoty_rachunkow)
srednia_kwota = suma_kwot / len(kwoty_rachunkow)

print(f'Maksymalna kwota: {maksymalna_kwota}')
print(f'Minimalna kwota: {minimalna_kwota}')
print(f'Suma kwot: {suma_kwot}')
print(f'Średnia kwota: {srednia_kwota}')

# rachunki b

rachunki = {'maj': 200, 'czerwiec': 230, 'lipiec': 300, 'sierpień': 330, 'marzec': 270}
kwoty_rachunkow = list(rachunki.values())
print("Rachunki za prąd:",rachunki)
maksymalna_kwota = max(kwoty_rachunkow)
minimalna_kwota = min(kwoty_rachunkow)
suma_kwot = sum(kwoty_rachunkow)
srednia_kwota = suma_kwot / len(kwoty_rachunkow)

print(f'Maksymalna kwota: {maksymalna_kwota}')
print(f'Minimalna kwota: {minimalna_kwota}')
print(f'Suma kwot: {suma_kwot}')
print(f'Średnia kwota: {srednia_kwota}')

ostatni = list(rachunki.keys())[-1]

ostatni_rachunek = rachunki[ostatni]

if ostatni_rachunek > srednia_kwota:
    print('Zacznij oszczędzać')
else:
    print('Jesteś bezpieczny')

# Zbiory

import random


def utworz_zbior(rozmiar):
    return {random.randint(0, 10) for _ in range(rozmiar)}


a = random.randint(3, 7)

b = random.randint(3, 7)

zbiór_X = utworz_zbior(a)
zbiór_Y = utworz_zbior(b)
print(f"Zbiór X ({a} elementów): {zbiór_X}")
print(f"Zbiór Y ({b} elementów): {zbiór_Y}")

# a

if 5 in zbiór_X:
    print("Zbiór X zawiera liczbę 5.")
else:
    print("Zbiór X nie zawiera liczby 5.")

# b

if zbiór_X.issubset(zbiór_Y):
    print("Zbiór X jest podzbiorem zbioru Y.")
else:
    print("Zbiór X nie jest podzbiorem zbioru Y.")

# c

if zbiór_Y.issubset(zbiór_X):
    print("Zbiór Y jest podzbiorem zbioru X.")
else:
    print("Zbiór Y nie jest podzbiorem zbioru X.")

# d

if zbiór_X.issuperset(zbiór_Y):
    print("Zbiór X jest nadzbiorem zbioru Y.")
else:
    print("Zbiór X nie jest nadzbiorem zbioru Y.")

# e

if zbiór_Y.issuperset(zbiór_X):
    print("Zbiór Y jest nadzbiorem zbioru X.")
else:
    print("Zbiór Y nie jest nadzbiorem zbioru X.")

# f

suma= zbiór_X.union(zbiór_Y)
print(f"Suma zbiorów X i Y: {suma}")

# g

roznica = zbiór_X.difference(zbiór_Y)

print(f"Różnica zbiorów X i Y: {roznica}")

# h

roznica = zbiór_Y.difference(zbiór_X)

print(f"Różnica zbiorów Y i X: {roznica}")

# i

iloczyn = zbiór_X.intersection(zbiór_Y)

print(f"Iloczyn zbiorów X i Y: {iloczyn}")

# j

roznica_sym = zbiór_X.symmetric_difference(zbiór_Y)

print(f"Różnica symetryczna zbiorów X i Y: {roznica_sym}")

# k

najwyzszy = max(max(zbiór_X), max(zbiór_Y))

print(f"Najwyższy element obu zbiorów: {najwyzszy}")

# l

pierwszyX = zbiór_X.pop()

zbiór_Y.add(pierwszyX)

print(f"Nowy zbiór Y({len(zbiór_Y)} elementów): {zbiór_Y}")

# m

zbiór_Y.update(zbiór_X)

print(f"Zbiór Y po skopiowaniu ({len(zbiór_Y)} elementów): {zbiór_Y}")

# n

zbiór_X.clear()
zbiór_Y.clear()

print(f"Zbiór X wyczyszczony({len(zbiór_X)} elementów): {zbiór_X}")
print(f"Zbiór Y wyczyszczony ({len(zbiór_Y)} elementów): {zbiór_Y}")
