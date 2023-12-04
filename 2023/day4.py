

from collections import defaultdict


with open("input4.txt") as f:
    lines = f.read().splitlines()

# print(lines)


def p1():
    res = 0
    for line in lines:
        _, numbers = line.split(": ")
        winning, having = numbers.split(" | ")
        winning = winning.split()
        having = having.split()
        count = len(set(winning).intersection(set(having)))
        if count:
            res += 2 ** (count - 1)
    return res

print(p1())



def p2():
    counts = defaultdict(int)
    for i, line in enumerate(lines, 1):
        counts[i] += 1
        _, numbers = line.split(": ")
        winning, having = numbers.split(" | ")
        winning = winning.split()
        having = having.split()
        count = len(set(winning).intersection(set(having)))
        for j in range(i + 1, i + count + 1):
            counts[j] += counts[i]
    return sum(counts.values())


print(p2())