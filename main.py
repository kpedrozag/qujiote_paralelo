from mpi4py import MPI
from mpi4py.MPI import ANY_SOURCE

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

file = open("quijote.txt", 'r', encoding='utf-8')
texto = file.read()
longitud = len(texto)

particion = int(longitud / size)

ini = particion * rank

if rank == size - 1:
    fin = (particion * (rank + 1)) + (longitud % size)
else:
    fin = particion * (rank + 1)

letras = []
contador = []
pos = 0
for i in range(ini, fin):
    bandera = False
    for j in range(len(letras)):
        if texto[i] == letras[j]:
            bandera = True
            pos = j
            break
    if bandera:
        contador[pos] += 1
    else:
        letras.append(texto[i])
        contador.append(1)

aux = []
if rank == 0:
        for i in range(1, size):
            comm.recv(aux, ANY_SOURCE)
            for j in range(len(aux[0])):
                if aux[0][j] in letras:
                    indice = letras.index(aux[0][j])
                    contador[indice] += aux[1][j]
                else:
                    letras.append(aux[0][j])
                    contador.append(aux[1][j])

else:
        comm.Send([letras, contador])
