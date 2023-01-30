from collections import deque
from utils import parse
from copy import deepcopy


def bfs(grid, src: tuple[int, int], dst: tuple[int, int]):
    grid[src[0]][src[1]] = "a"
    grid[dst[0]][dst[1]] = "z"

    queue, visited, steps = deque([src]), set(), 0
    visited.add(src)
    while queue:
        n = len(queue)
        for _ in range(n):
            r, c = queue.popleft()
            if r == dst[0] and c == dst[1]:
                return steps

            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if (
                    0 <= nr <= len(grid) - 1
                    and 0 <= nc <= len(grid[0]) - 1
                    and ord(grid[nr][nc]) - ord(grid[r][c]) <= 1
                    and (nr, nc) not in visited
                ):
                    visited.add((nr, nc))
                    queue.append((nr, nc))
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
