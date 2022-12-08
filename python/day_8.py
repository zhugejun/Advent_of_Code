import math
from utils import parse


def day8_1():
    data = parse(8)
    res = 0
    m, n = len(data), len(data[0])

    for r in range(m):
        for c in range(n):
            res += (
                all(data[i][c] < data[r][c] for i in range(r))
                or all(data[i][c] < data[r][c] for i in range(r + 1, m))
                or all(data[r][j] < data[r][c] for j in range(c))
                or all(data[r][j] < data[r][c] for j in range(c + 1, n))
            )
    return res


print(day8_1())


def day8_2():
    data = parse(8)
    m, n = len(data), len(data[0])
    res = []
    for r in range(m):
        for c in range(n):
            score = [0, 0, 0, 0]
            # down
            for i in range(r + 1, m):
                score[0] += 1
                if data[i][c] >= data[r][c]:
                    break

            # up
            for i in range(r - 1, -1, -1):
                score[1] += 1
                if data[i][c] >= data[r][c]:
                    break

            # left
            for j in range(c - 1, -1, -1):
                score[2] += 1
                if data[r][j] >= data[r][c]:
                    break

            # right
            for j in range(c + 1, n):
                score[3] += 1
                if data[r][j] >= data[r][c]:
                    break

            res.append(math.prod(score))
    return max(res)


print(day8_2())
