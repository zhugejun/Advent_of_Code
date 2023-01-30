from utils import parse
from itertools import product, count


def draw(x1, y1, x2, y2):
    if x1 > x2:
        return draw(x2, y1, x1, y2)
    if y1 > y2:
        return draw(x1, y2, x2, y1)
    return product(range(x1, x2 + 1), range(y1, y2 + 1))


def adj(x, y):
    return (x, y + 1), (x - 1, y + 1), (x + 1, y + 1)


def day14_1():
    data = parse(14)

    rocks = set()
    for line in data:
        cords = line.split(" -> ")
        for a, b in zip(cords, cords[1:]):
            rocks.update(draw(*eval(a), *eval(b)))

    max_y = max(y for _, y in rocks)
    i = 0
    for i in count():
        curr = (500, 0)
        while curr[1] < max_y:
            try:
                curr = next(x for x in adj(*curr) if x not in rocks)
            except StopIteration:
                break
        else:
            return i
        rocks.add(curr)


print(day14_1())


def day14_2():
    data = parse(14)

    rocks = set()
    for line in data:
        cords = line.split(" -> ")
        for a, b in zip(cords, cords[1:]):
            rocks.update(draw(*eval(a), *eval(b)))

    max_y = max(y for _, y in rocks)
    i = 0
    for i in count():
        curr = (500, 0)
        while True:
            try:
                curr = next(
                    x for x in adj(*curr) if x not in rocks and x[1] < max_y + 2
                )
            except StopIteration:
                break
        if curr == (500, 0):
            return i + 1
        rocks.add(curr)


print(day14_2())
