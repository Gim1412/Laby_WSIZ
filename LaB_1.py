# Cena biletu
print("Zadanie 1. Cena biletu")

x = int(input("Podaj swój wiek:"))
print("Wiek:", x, "lat(a)")
if x < 4:
    print("Wstęp jest bezpłatny")
elif x <= 18:
    print("Cena biletu: 10zł")
else:
    print("Cena biletu: 20zł")


# Zadanie 2
print("Zadanie 2.")

print("Wielkość liter")

x=input("Wpisz dowolną literę:")
if x.isupper():
    print("Wielka litera")
elif x.islower():
    print("Mała litera")
else:
    print("Spróbuj ponownie")

 # Zadanie 3



print("Kalkulator")

x = int(input("Podaj pierwszą liczbę:"))
y = int(input("Podaj drugą liczbę:"))

print("x =", x)
print("y =", y)

print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnożenie")
print("4. Dzielenie")
print("5. Potęgowanie")

z=int(input("Podaj numer operacji od 1 do 5:"))
print("operacja nr:",z)

if z == 1:
    print("Suma x+y=",x+y)
elif z == 2:
    print("Różnica x-y=", x-y)
elif z == 3:
    print("Iloczyn x*y=",x*y)
elif z == 4:
    print("Iloraz x/y=",x/y)
elif z == 5:
    print("Potęgowanie x**y=", x ** y)
else:
    print("Spróbuj jeszcze raz")

# Równanie kwadratowe

print("Równanie kwadratowe")
from math import sqrt

a = int(input("Podaj a:"))
b = int(input("Podaj b:"))
c = int(input("Podaj c:"))
print(a,"*x^2+",b,"*x+",c,"=0")
delta = b*b-4*a*c


if delta < 0:
    print("Brak rozwiązań")
elif delta == 0:
    print("x=", -b/2*a)
else:
    deltap = sqrt(delta)
    print("x1 =", (-b-deltap/2*a))
    print("x2 =", (-b+deltap/2*a))


# Zadanie 5

print("in progress...")