import random
import math


def procedure():
    circle_count = 0
    npoints = 1000000
    for i in range(npoints):
        if InsideCircle(random.uniform(0.0, 1.0), random.uniform(0.0, 1.0)):
            circle_count += 1
    pi_value = 4.0 * circle_count / npoints
    print("The PI value is:", pi_value)


def InsideCircle(x, y):
    return math.sqrt(math.pow(x, 2) + math.pow(y, 2)) <= 1


procedure()