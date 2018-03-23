from mpi4py import MPI
import random
import math
import numpy


def procedure(p, npoints):
    circle_count = 0
    num = npoints / p
    for i in range(int(num)):
        if math.sqrt(math.pow(random.uniform(0.0, 1.0), 2) + math.pow(random.uniform(0.0, 1.0), 2)) <= 1:
            circle_count += 1
    return circle_count


def InsideCircle(x, y):
    return math.sqrt(math.pow(x, 2) + math.pow(y, 2)) <= 1


if __name__ == '__main__':
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    np = 10000  # number of points

    random.seed(rank)

    summa = numpy.zeros(1)
    recv_buffer = numpy.zeros(1)

    summa[0] = procedure(size, np)

    if rank == 0:
        total = summa[0]
        for i in range(1, size):
            comm.Recv(recv_buffer, MPI.ANY_SOURCE)
            total += recv_buffer[0]

        print("The value of pi is", 4.0 * total / np)
    else:
        comm.Send(summa, dest=0)
