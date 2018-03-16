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

letras = {}
pos = 0
for i in range(ini, fin):
    if texto[i] in letras.keys():
        letras[texto[i]] += 1
    else:
        letras[texto[i]] = 1

buffer = {}
if rank == 0:
    for i in range(1, size):
        comm.recv(buffer, ANY_SOURCE)
        for key, value in buffer.items():
            if key in letras.keys():
                letras[key] += value
            else:
                letras[key] = value
else:
    comm.send(letras)

