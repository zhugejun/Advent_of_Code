from utils import parse


# ref: https://github.com/kwshi/advent-of-code/blob/main/python/2022/07.py
def data():
    sizes, cwd = {(): 0}, []
    lines = parse(7)
    for line in lines:
        match line.split():
            case ["$", "cd", "/"]:
                cwd = []
            case ["$", "cd", ".."]:
                cwd.pop()
            case ["$", "cd", d]:
                cwd.append(d)
            case ["$", "ls"]:
                pass
            case ["dir", d]:
                sizes[tuple(cwd + [d])] = 0
            case [n, _]:
                for i in range(len(cwd) + 1):
                    sizes[tuple(cwd[:i])] += int(n)
            case _:
                assert False, f"unrecognized command {line}"
    return sizes


# data()


def day7_1():
    sizes = data()
    return sum(v for v in sizes.values() if v <= 100_000)


def day7_2():
    sizes = data()
    free = 70_000_000 - sizes[()]
    return min(v for v in sizes.values() if v + free >= 30_000_000)


print(day7_1())
print(day7_2())
