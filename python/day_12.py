from collections import deque
from utils import parse
from copy import deepcopy


def bfs(grid, src: tuple[int, int], dst: tuple[int, int]):
    grid[src[0]][src[1]] = "a"
    grid[dst[0]][dst[1]] = "z"

    queue = deque([src])
    visited = set()
    visited.add(src)
    steps = 0
    while queue:
        n = len(queue)
        for _ in range(n):
            r, c = queue.popleft()
            if r == dst[0] and c == dst[1]:
                # for row in grid:
                #     print("".join(row))
                return steps

            visited.add((r, c))

            # left
            if (
                r - 1 >= 0
                and ord(grid[r - 1][c]) - ord(grid[r][c]) <= 1
                and (r - 1, c) not in visited
            ):
                queue.append((r - 1, c))

            # up
            if (
                c - 1 >= 0
                and ord(grid[r][c - 1]) - ord(grid[r][c]) <= 1
                and (r, c - 1) not in visited
            ):
                queue.append((r, c - 1))

            # down
            if (
                r + 1 <= len(grid) - 1
                and ord(grid[r + 1][c]) - ord(grid[r][c]) <= 1
                and (r + 1, c) not in visited
            ):
                queue.append((r + 1, c))

            # right
            if (
                c + 1 <= len(grid[0]) - 1
                and ord(grid[r][c + 1]) - ord(grid[r][c]) <= 1
                and (r, c + 1) not in visited
            ):
                queue.append((r, c + 1))
            grid[r][c] = "#"
        steps += 1
    return -1


def day12_1():
    grid = parse(12)

    grid = [list(row) for row in grid]
    s = (20, 0)
    d = (20, 36)
    return bfs(grid, (20, 0), (20, 36))


print(day12_1())


def day12_2():
    grid = parse(12)
    dst = (20, 36)

    steps = float("inf")
    grid = [list(row) for row in grid]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] in ["a", "S"]:
                src = (i, j)
                curr_steps = bfs(deepcopy(grid), src, dst)
                if curr_steps != -1:
                    steps = min(steps, curr_steps)

    return steps


print(day12_2())
