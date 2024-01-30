# Laboratorium nr 2

# Zad. 1
print("Zadanie nr 1")
x=int(input( "podaj pierwszą liczbę:"))
y=int(input("podaj drugą liczbę:"))
print("x=",x)
print("y=",y)

start = min(x, y)
koniec = max(x, y)

print(f"Liczby od {start} do {koniec} to:")
for liczba in range(start, koniec + 1):
    print(liczba)

# Zad. 2
print("Zadanie nr 2")
def funkcja_(x):
    return 2 * x**2 - 5 * x - 8

def main():
    x_min = -4
    x_max = 4
    krok = 0.5

    print(f"{'x':<5}{'y':<10}")
    print("-" * 15)

    x = x_min
    while x <= x_max:
        y = funkcja_(x)
        print(f"{x:<5}{y:<10}")
        x += krok

if __name__ == "__main__":
    main()

# Zad. 3
print("Zadanie nr 3")

while True:
    liczba = int(input("Podaj liczbę całkowitą:"))

    if liczba < 0:
        print("Podana liczba jest ujemna.")
        break
    else:
        print("Podana liczba jest dodatnia")

# Zad. 4
print("Zadanie nr 4")
x=int(input( "podaj pierwszą liczbę:"))
y=int(input("podaj drugą liczbę:"))
print("x=",x)
print("y=",y)

start = min(x, y)
koniec = max(x, y)

print(f"Liczby od {start} do {koniec} to:")
for liczba in range(start, koniec + 1):
    if liczba % 2 == 1:
        continue
    print(liczba)

# Ciąg 1

print("Ciąg 1")
for i in range(1, 101):
    print(i, end=", ")

# Ciąg 2

print("Ciąg 2")
for i in range(100, -1, -1):
    print(i, end=", ")

# Ciąg 3
print("Ciąg 3")
for i in range(7, 77, 7):
    print(i, end=", ")

# Ciąg 4

print("Ciąg 4")
for i in range(20, -1, -2):
    print(i, end=", ")

# Gwiazdki

liczba_gwiazd = int(input("Podaj liczbę gwiazd: "))

for i in range(liczba_gwiazd):
    print("* " * liczba_gwiazd)

# Choinka 1

height = int(input("Wprowadź wysokość choinki"))
for i in range(1, height + 1):
        print('* ' * i)

# Choinka 2

height = int(input("Podaj liczbę całkowitą"))

for i in range(1, height + 1):
    spaces = ' ' * (height - i)
    stars = '* ' * i
    print(f"{spaces}{stars}")

# Ciąg arytmetyczny

while True:
    try:
        n = int(input("Podaj liczbę naturalną: "))

        if n > 0:
            break
        else:
            print("Spróbuj ponownie.")
    except ValueError:
        print("Coś poszło nie tak.")
print("Liczba naturalna:", n)

a = int(input("Podaj liczę a"))
r = int(input("Podaj liczę r"))

print("n = ", n)
print("a = ", a)
print("r = ", r)
print("Wyrazy ciągu")
for x in range (n):
    wyrazy = x + (n - 1) * r
    print( wyrazy)

# n!

while True:
    try:
        n = int(input("Podaj liczbę naturalną: "))

        if n > 0:
            break
        else:
            print("Spróbuj ponownie.")
    except ValueError:
        print("Coś poszło nie tak.")
print(" Liczba naturalna:", n)

n = int(input("Podaj liczbę naturalną:"))


def silnia(n):

    wynik = 1
    for x in range(1, n + 1):
        wynik *= x

    return wynik


z = silnia(n)

print("n!=", z)
