

from functools import reduce
import math
from operator import mul

test = """Time:      7  15   30
Distance:  9  40  200
"""


with open("input6.txt") as f:
    lines = f.read().splitlines()



def dist(time):
    res = []
    for i in range(time):
        d = i * (time - i)
        res.append(d)
    return res
    

# lines = test.splitlines()
times = [int(x) for x in lines[0].split()[1:]]
distances = [int(x) for x in lines[1].split()[1:]]

result = []
for i, (time, distance) in enumerate(zip(times, distances)):
    dists = dist(time)
    result.append(sum([dist > distance for dist in dists]))

print(reduce(mul, result, 1))



# part 2
def beat(time, record):
    res =  0
    for i in range(time):
        d = i * (time - i)
        if d > record:
            res += 1
        elif d < record and res > 0:
            return res


time =  int(lines[0].split(":")[1:][0].replace(" ", ""))
distance = int(lines[1].split(":")[1:][0].replace(" ", ""))

print(beat(time, distance))


# optimized
# it's a quadratic equation

a = (time - math.sqrt(time ** 2 - 4 * distance)) / 2
b = (time + math.sqrt(time ** 2 - 4 * distance)) / 2

print(math.floor(b) - math.ceil(a) + 1)
