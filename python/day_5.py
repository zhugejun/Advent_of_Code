from collections import defaultdict
from utils import parse


def day5_1():
    data = parse(5)
    moves = data[10:]

    stacks = defaultdict(list)
    for row in data[:8][::-1]:
        for i, j in enumerate(range(1, 34, 4)):
            if row[j] != " ":
                stacks[i + 1].append(row[j])

    for move in moves:
        _, num, _, src, _, dst = move.split(" ")

        for _ in range(int(num)):
            crate = stacks[int(src)].pop()
            stacks[int(dst)].append(crate)

    tops = [stacks[i][-1] for i in range(1, 10)]
    return "".join(tops)


print(day5_1())


def day5_2():
    data = parse(5)
    moves = data[10:]

    stacks = defaultdict(list)
    for row in data[:8][::-1]:
        for i, j in enumerate(range(1, 34, 4)):
            if row[j] != " ":
                stacks[i + 1].append(row[j])

    for i, move in enumerate(moves):
        _, num, _, src, _, dst = move.split(" ")

        pos = len(stacks[int(src)]) - int(num)
        stacks[int(src)], crates = stacks[int(src)][:pos], stacks[int(src)][pos:]
        stacks[int(dst)] += crates

    tops = [stacks[i][-1] for i in range(1, 10)]
    return "".join(tops)


print(day5_2())
