# https://pythonprogramming.net/mpi-gather-command-mpi4py-python/?completed=/scatter-gather-mpi-mpi4py-tutorial/
from mpi4py import MPI
from mpi4py.MPI import ANY_SOURCE

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

file = open("quijote.txt", 'r', encoding='utf-8')
texto = file.read()
longitud = len(texto)

if rank == 0:
    data = []
    longitud = len(texto)
    particion = int(longitud / size)
    for i in range(size):
        ini = particion * i
        if i == size - 1:
            fin = particion * (i + 1) + (longitud % size)
        else:
            fin = particion * (i + 1)
        data.append(texto[ini:fin])
else:
    data = None

data = comm.scatter(data, root=0)

print('rank:', rank, 'data: ', type(data))

letras = []
contador = []
pos = 0

for i in range(len(data)):
    bandera = False
    for j in range(len(letras)):
        if data[i] == letras[j]:
            bandera = True
            pos = j
            break
    if bandera:
        contador[pos] += 1
    else:
        letras.append(data[i])
        contador.append(1)

listas = comm.gather([letras, contador], root=0)
letras = []
contador = []

if rank == 0:
    for i in range(len(listas)):
        for j in range(len(listas[i][0])):
            if listas[i][0][j] in letras:
                indice = letras.index(listas[i][0][j])
                contador[indice] += listas[i][1][j]
            else:
                letras.append(listas[i][0][j])
                contador.append(listas[i][1][j])

    for i in range(len(letras)):
        print('Caracter:', letras[i], 'repetido', contador[i], 'veces', sep='\t')
