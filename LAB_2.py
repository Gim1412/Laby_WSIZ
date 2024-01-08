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
