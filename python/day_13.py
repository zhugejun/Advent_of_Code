from functools import total_ordering
from utils import parse
import ast
import math
from functools import cmp_to_key


def is_lower(f, s):
    # both integer
    if type(f) == int and type(s) == int:
        return (f < s) - (f > s)
    # both list
    if type(f) == list and type(s) == list:
        for a, b in zip(f, s):
            comp = is_lower(a, b)
            if comp:
                return comp
        return (len(f) < len(s)) - (len(f) > len(s))
    # int and list
    if type(f) == int and type(s) == list:
        return is_lower([f], s)
    if type(f) == list and type(s) == int:
        return is_lower(f, [s])


def day13_1():
    data = parse(13)
    res = 0
    for p, i in enumerate(range(0, len(data), 3)):
        first = ast.literal_eval(data[i])
        second = ast.literal_eval(data[i + 1])

        if is_lower(first, second) == 1:
            res += p + 1
    return res


print(day13_1())


def day13_2():
    dividers = [[[2]], [[6]]]
    packets = [ast.literal_eval(row) for row in parse(13) if row] + dividers
    packets.sort(key=cmp_to_key(is_lower), reverse=True)
    return math.prod(packets.index(x) + 1 for x in dividers)


print(day13_2())
