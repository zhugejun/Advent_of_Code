from utils import parse


class Position(tuple):
    def __add__(self, other):
        return Position(p1 + p2 for p1, p2 in zip(self, other))

    def __sub__(self, other):
        return Position(p1 - p2 for p1, p2 in zip(self, other))


DIRS = {
    "U": Position((0, 1)),
    "D": Position((0, -1)),
    "L": Position((-1, 0)),
    "R": Position((1, 0)),
}


def move(h, t):
    diff = Position(min(1, max(-1, x)) for x in h - t)
    if diff == h - t:
        return t
    return t + diff


def day9_1():
    data = parse(9)
    H = Position((0, 0))
    T = Position((0, 0))
    visited = set()
    visited.add(T)
    for line in data:
        direc, num = line.split(" ")
        for _ in range(int(num)):
            H += DIRS[direc]
            T = move(H, T)
            visited.add(T)
    return len(visited)


print(day9_1())


def day9_2():
    data = parse(9)
    rope = [Position((0, 0)) for _ in range(10)]
    visited = set()

    for line in data:
        direc, num = line.split(" ")
        for _ in range(int(num)):
            rope[0] += DIRS[direc]
            for j in range(len(rope) - 1):
                rope[j + 1] = move(rope[j], rope[j + 1])

            visited.add(rope[9])
    return len(visited)


print(day9_2())
