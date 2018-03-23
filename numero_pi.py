import random
import math

def procedure():
    circle_count = 0
    npoints = 1000000
    for i in range(npoints):
        if math.sqrt(math.pow(random.uniform(0.0, 1.0), 2) + math.pow(random.uniform(0.0, 1.0), 2)) <= 1:
            circle_count += 1
    pi_value = 4.0 * circle_count / npoints
    print("The PI value is:", pi_value)

procedure()
