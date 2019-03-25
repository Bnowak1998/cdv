print("CDV")
print(2)

#potęga
potega = 2 ** 10
print (potega)

#pobieranie danych z klawiatury
imie = input()
print ("Twoje imię podane z klawiatury: " +imie)

nazwisko=input()
print("Twoje imię: " + imie + ",Twoje nazwisko: " + nazwisko)

dlugosc=len(nazwisko)
print(type(dlugosc))
print("Długość nazwiska: ",  dlugosc)


dlugosc=str(dlugosc)
print(type(dlugosc))
print("Długość nazwiska: "+  dlugosc)
print("Podaj wiek: ",end="")
wiek=input()
print(type(wiek))
print("Twój wiek: "+wiek +" lat")

nazwisko = 'Kowalski'

pierwszyZnak = nazwisko[0];
print(pierwszyZnak)
ostatniZnak = nazwisko[len(nazwisko)-1]
print(ostatniZnak)

ostatniZnak = nazwisko[-1]
x="5"
print(type(x))
x=int(x)
print(type(x))

text = "Jan"*2
print(text)
print(type(text))

y = 6
print(type(y))
y = y / 2
print(type(y))
print(y)

wiek = 21
print("Twój wiek: ", wiek)
wiek = str(wiek)
print("Twój wiek: "+ wiek)

nazwisko = "Jankowski"
print(nazwisko[0])
print(nazwisko[0:3])
print(nazwisko[-2])
print(nazwisko[-2:])
