from collections import defaultdict
from functools import reduce
from itertools import product

# part 1

result = 0
with open("input2.txt") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        game, bag = line.split(": ")
        number = game.split()[1]
        sts = bag.split("; ")
        valid = True
        for st in sts:
            counts = defaultdict(int)
            for cubes in st.split(", "):
                count, color = cubes.split()
                counts[color] += int(count)
            if counts["red"] > 12 or counts["green"] > 13 or counts["blue"] > 14:
                valid = False
        if valid:
            result += int(number)

    print(result)



# part 2

result = 0
with open("input2.txt") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        game, bag = line.split(": ")
        number = game.split()[1]
        sts = bag.split("; ")

        counts = defaultdict(int)
        for st in sts:
            for cubes in st.split(", "):
                count, color = cubes.split()
                counts[color] = max(int(count), counts[color])
        result += reduce(lambda x, y: x * y, counts.values())


    print(result)






