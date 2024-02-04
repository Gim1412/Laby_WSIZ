# Laboratorium 4

# 1 Pole koła
r = int(input("Podaj promień koła:"))


def pole_kola(r):
    if r < 0:
        print("Promień nie może być ujemny.")
        return


pole = 3.14 * r ** 2

print("Pole koła o promieniu r:", r, "=", pole)


# 2  Trapez

def pole_trapezu(h, a, b):
    poletrap = 0.5 * (a + b) * h
    return poletrap


h = int(input("Podaj wysokość trapezu:"))
a = int(input("Podaj długość 1 podstawy trapezu:"))
b = int(input("Podaj długość 2 podstawy trapezu:"))
wynik = pole_trapezu(h, a, b)
print(f"Pole trapezu: {wynik}")

# Imię wiek

def imie_wiek(imie, wiek=20):
    """Tak funkcja wyświetla imię oraz wiek"""
    print("Imię:", imie)
    print("Wiek:", wiek)

imie = "ADAM"


print(imie_wiek.__doc__)

imie_wiek(imie)

# Dodatnia

def dodatnia(x):
    if x > 0:
        print(f"Liczba x jest dodatnia")
    else:
        print(f"Liczba x nie jest dodatnia")

dodatnia(0)


# BMI
def liczbmi(waga, wzrost):
    bmi = waga / (wzrost ** 2)

    if bmi < 18.5:
        zakres = "niedowaga"
    elif 18.5 <= bmi < 24.9:
        zakres = "w normie"
    elif 25 <= bmi < 29.9:
        zakres = "nadwaga"
    else:
        zakres = "otyłość"

    return bmi, zakres


waga = float(input("Podaj wagę  (kg): "))
wzrost = float(input("Podaj wzrost (m) : "))

bmi, zakres = liczbmi(waga, wzrost)

print(f"BMI wynosi: {bmi:.2f}")
print(f"Zakres BMI: {zakres}")

# Odwracanie string

def odwroc_string(tekst):
    return tekst[::-1]


tekst = "dobranoc"
tekst2 = odwroc_string(tekst)

print(f"odwrotny: {tekst2}")

# Potęga

def potega(a, n):

    if n == 0:
        return 1
    elif n > 0:

        return a * potega(a, n - 1)
    else:

        return 1 / potega(a, -n)


a = 4
n = 2
wynik = potega(a, n)
print(f"{a} **  {n} = {wynik}")

# Fibonacci

def fibo(n):
    if n <= 0:
        return "Błąd"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:

        return fibo(n - 1) + fibo(n - 2)

n = 3
wynik = fibo(n)
print(f"{n}-ty wyraz ciągu: {wynik}")



