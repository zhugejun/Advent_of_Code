
test = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""



def extrapolate(arr):
    res = [arr]
    while len(set(arr)) != 1:
        arr = [arr[i] - arr[i - 1] for i in range(1, len(arr))]
        res.append(arr)
    res = res[::-1]
    for i, arr in enumerate(res[1:], 1):
        arr.append(arr[-1] + res[i - 1][-1])
    return arr




with open("2023/input9.txt") as f:
    lines = f.read().splitlines()


# lines = test.splitlines()

res = 0
for i, line in enumerate(lines):
    line = [int(x) for x in line.split()]
    res += extrapolate(line)[-1]
print(res)



# part 2


def extrapolate(arr):
    arrs = [arr]
    while len(set(arr)) != 1:
        arr = [arr[i] - arr[i - 1] for i in range(1, len(arr))]
        arrs.append(arr)
    arrs = arrs[::-1]
    
    last = arrs[0][0]
    for i, arr in enumerate(arrs[1:], 1):
        last = arr[0] - last
    return last


res = 0
for i, line in enumerate(lines):
    line = [int(x) for x in line.split()]
    res += extrapolate(line)
print(res)




# https://github.com/oliver-ni/advent-of-code/blob/master/py/2023/day09.py
from itertools import pairwise


def seq(ints):
    if all(ints == 0 for ints in ints):
        return 0
    diffs = [b - a for a, b in pairwise(ints)]
    return ints[-1] + seq(diffs)


def p1(f):
    return sum(seq([int(x) for x in line.split()]) for line in f)


def p2(f):
    return sum(seq([int(x) for x in line.split()[::-1]]) for line in f)


print(p1(open("2023/input9.txt")))
print(p2(open("2023/input9.txt")))