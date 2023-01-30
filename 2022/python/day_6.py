from utils import parse


def day6_1():
    data = parse(6)[0]
    for i in range(len(data) - 4):
        if len(set(data[i : i + 4])) == 4:
            return i + 4


print(day6_1())


def day6_2():
    data = parse(6)[0]
    for i in range(len(data) - 14):
        if len(set(data[i : i + 14])) == 14:
            return i + 14


print(day6_2())
