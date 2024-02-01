# Laboratorium 3

# Zadanie 1

tekst = "Rzeszów jest piękny"

print(tekst[0])
print(tekst[6], tekst[9], tekst[12],tekst[1])

# Zadanie 2

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
print(imie[0],nazwisko[0])

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
lista2=lista*2
print(lista2)


# Część druga






