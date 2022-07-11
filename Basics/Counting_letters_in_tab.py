napis = "Ala ma kota"
tablica = napis.split(" ")
print("Liczba wyrazów", len(tablica))
print(tablica)

i=0
x=0
while x < len(tablica):
    i += len(tablica[x])
    x += 1

print("Liczba liter", i)
print("Częstotliwość:")
print("a", napis.count("a"))
print("l", napis.count("l"))
print("m", napis.count("m"))
print("k", napis.count("k"))
print("t", napis.count("t"))


