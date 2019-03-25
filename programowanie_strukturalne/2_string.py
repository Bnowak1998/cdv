tekst = "Anna, paweł, JulIA"

lista = tekst.split(",")
print(tekst)
print(lista)
print(type(lista))

imie1 = lista[0]
print(imie1)

print("twoje imię:", imie1)

imieDuze = imie1.upper()
print(imieDuze)

imieMale = imie1.lower
print(imieMale)
print(imie1)

print("\nPodaj swoje nazwisko: ", end="")
nazwisko = input()
zawartosc = nazwisko.isalpha()
print(zawartosc)
#sprawdzić dlaczego przy liczbach jest false

nazwisko = ""
print(nazwisko.isalpha())

text1 = "Julia\n"
text2 = "Nowak"
print(text1+ text2)
text1 = text1.rstrip()
print(text1 + text2)
print(text1 + " "+ text2)

#wyświetlanie łańcucha znaków

#wszystkie wersje Pythona
text = "%a, Java i %a"% ("PHP","Python")
print(text)


print()
