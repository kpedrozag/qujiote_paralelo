from mpi4py import MPI
from mpi4py.MPI import ANY_SOURCE, FLOAT
import random
import math


NPOINTS = 10000.


def procedure(p):
    circle_count = 0.
    npoints = NPOINTS

    num = npoints / p

    for i in range(int(num)):
        if InsideCircle(random.uniform(0.0, 1.0), random.uniform(0.0, 1.0)):
            circle_count += 1.
    return circle_count


def InsideCircle(x, y):
    return math.sqrt(math.pow(x, 2) + math.pow(y, 2)) <= 1


if __name__ == '__main__':
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    aux = []
    summa = procedure(size)
    if rank == 0:
        for i in range(1, size):
            comm.recv(aux, ANY_SOURCE)
        summa += sum(aux)

        print("The value of pi is", 4. * NPOINTS / summa)
    else:
        comm.send([summa], dest=0)