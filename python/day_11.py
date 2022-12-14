from collections import defaultdict
from math import prod
from utils import parse


# https://github.com/oliver-ni/advent-of-code/blob/master/py/2022/day11.py
def parse_monkey(lines):
    return {
        "items": [int(x) for x in lines[1][18:].split(",")],
        "op": lambda old: eval(lines[2][19:]),
        "test": lambda x: x % int(lines[3][21:]) == 0,
        "testnum": int(lines[3][21:]),
        "throw": {
            True: int(lines[4][29:]),
            False: int(lines[5][30:]),
        },
    }


def day11_1():
    with open(f"data/input11.txt", "r") as f:
        monkeys = [parse_monkey(m.splitlines()) for m in f.read().split("\n\n")]
        active = defaultdict(int)

        for r in range(20):
            print(f"Round: {r}")
            for i, monkey in enumerate(monkeys):
                for item in monkey["items"]:
                    active[i] += 1
                    new = monkey["op"](item) // 3
                    test = monkey["test"](new)
                    throw = monkey["throw"][test]
                    monkeys[throw]["items"].append(new)
                monkey["item"] = []
        active.values().sort(reverse=True)
        return active[0] * active[1]


def day11_2():
    with open(f"data/input11.txt", "r") as f:
        monkeys = [parse_monkey(m.splitlines()) for m in f.read().split("\n\n")]
        active = defaultdict(int)
        mod = prod([m["testnum"] for m in monkeys])

        for r in range(20):
            print(f"Round: {r}")
            for i, monkey in enumerate(monkeys):
                for item in monkey["items"]:
                    active[i] += 1
                    new = monkey["op"](item) % mod
                    test = monkey["test"](new)
                    throw = monkey["throw"][test]
                    monkeys[throw]["items"].append(new)
                monkey["item"] = []
        active.values().sort(reverse=True)
        return active[0] * active[1]


# https://github.com/mrphlip/aoc/blob/master/2022/11.py
from copy import deepcopy
from math import lcm
from functools import reduce

dat = [
    (
        [65, 58, 93, 57, 66],
        "*",
        7,
        19,
        6,
        4,
    ),
    (
        [76, 97, 58, 72, 57, 92, 82],
        "+",
        4,
        3,
        7,
        5,
    ),
    (
        [90, 89, 96],
        "*",
        5,
        13,
        5,
        1,
    ),
    (
        [72, 63, 72, 99],
        "^",
        None,
        17,
        0,
        4,
    ),
    (
        [65],
        "+",
        1,
        2,
        6,
        2,
    ),
    (
        [97, 71],
        "+",
        8,
        11,
        7,
        3,
    ),
    (
        [83, 68, 88, 55, 87, 67],
        "+",
        2,
        5,
        2,
        1,
    ),
    (
        [64, 81, 50, 96, 82, 53, 62, 92],
        "+",
        5,
        7,
        3,
        0,
    ),
]
mod = reduce(lcm, [i[3] for i in dat])
origdat = deepcopy(dat)

count = [0] * len(dat)


def turn(part1):
    for n, m in enumerate(dat):
        for i in m[0]:
            if m[1] == "+":
                i += m[2]
            elif m[1] == "*":
                i *= m[2]
            else:
                i *= i
            if part1:
                i //= 3
            else:
                i %= mod
            target = m[4] if i % m[3] == 0 else m[5]
            dat[target][0].append(i)
            count[n] += 1
        m[0][:] = []


for i in range(20):
    turn(True)
count.sort()
print(count[-1] * count[-2])

dat = origdat
count = [0] * len(dat)
for i in range(10000):
    turn(False)
count.sort()
print(count[-1] * count[-2])
