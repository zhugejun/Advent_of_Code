from collections import defaultdict



with open("2023/input5.txt") as f:
    lines = f.read().split("\n\n")


seeds = [int(x) for x in lines[0].split(": ")[1].split()]

for i, line in enumerate(lines[1:], 1):
    _, *numbers = line.splitlines()
    numbers = [[int(x) for x in number.split()] for number in numbers]
    ranges = [(range(x, x + z), range(y, y + z)) for x, y, z in numbers]

    def find_number(seed):
        for a, b in ranges:
            if seed in b:
                return a.start + seed - b.start
        return seed

    seeds = [find_number(x) for x in seeds]

print(min(seeds))


# part 2
# reference: https://github.com/oliver-ni/advent-of-code/blob/master/py/2023/day05.py
# still confused about the logic

with open("2023/input5.txt") as f:
    seeds, *numbers = f.read().split("\n\n")
    seeds = seeds.split(": ")[1]
    seeds = [int(x) for x in seeds.split()]
    seeds = [range(x, x + y) for x, y in zip(seeds[::2], seeds[1::2])]

# print(seeds)


for i, line in enumerate(lines[1:], 1):
    _, *numbers = line.splitlines()
    numbers = [[int(x) for x in number.split()] for number in numbers]
    ranges = [(range(x, x + z), range(y, y + z)) for x, y, z in numbers]

    new_seeds = []
    for seed in seeds:
        for t, f in ranges:
            offset = t.start - f.start
            if seed.stop <= f.start or seed.start >= f.stop:
                continue
            # intersection 
            i = range(max(seed.start, f.start), min(seed.stop, f.stop))
            # left side
            l = range(seed.start, i.start)
            # right side
            r = range(i.stop, seed.stop)
            if l:
                seeds.append(l)
            if r:
                seeds.append(r)
            new_seeds.append(range(i.start + offset, i.stop + offset))
            break
        else:
            new_seeds.append(seed)
    seeds = new_seeds

print(min(seed.start for seed in seeds))
