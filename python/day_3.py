from utils import parse
from string import ascii_lowercase, ascii_uppercase


def _common_char(s1, s2):
    for c in s1:
        if c in s2:
            return c
    return -1


def common_char(s):
    mid = len(s) // 2
    return _common_char(s[:mid], s[mid:])


def common_chars(s1, s2):
    res = ""
    for c in s1:
        if c in s2:
            res += c
    if len(res) > 1:
        return "".join(list(set(res)))
    return res


def priority(c):
    if c in ascii_lowercase:
        return ord(c) - ord("a") + 1
    return ord(c) - ord("A") + 27


def day3_1():
    data = parse(3)
    priorities = [priority(common_char(s)) for s in data]
    return sum(priorities)


def day3_2():
    data = parse(3)
    n = len(data)
    res = 0
    for i in range(0, n, 3):
        group = data[i : i + 3]
        chars = common_chars(group[0], group[1])
        char = common_chars(chars, group[2])
        res += priority(char)
    return res


print(day3_2())
