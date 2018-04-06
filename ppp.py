texto = ""
cadena = "0123456789"
for i in range(10):
    texto += cadena
texto += "---"
print(texto)

data = []
size = 4
longitud = len(texto)
particion = int(longitud / size)
for i in range(size):
    ini = particion * i
    if i == size - 1:
        fin = particion * (i + 1) + (longitud % size)
    else:
        fin = particion * (i + 1)
    data.append(texto[ini:fin])

print(data)
print(len(data))
print(len(data[0]))
