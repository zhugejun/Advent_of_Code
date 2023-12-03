from collections import defaultdict
import re


def extract_numbers_and_indexes(s):
    matches = re.finditer(r"\d+", s)
    result = [(match.group(), match.start(), match.end()) for match in matches]
    return result


# print(extract_numbers_and_indexes("467..114..477"))


result = 0

with open("input3.txt") as f:
    lines = f.read().splitlines()
    for i, line in enumerate(lines):
        numbers = extract_numbers_and_indexes(line)
        for number, start, end in numbers:
            idxs = [(i, start - 1), (i, end)] 
            idxs += [(i - 1, j) for j in range(start - 1, end + 1)]
            idxs += [(i + 1, j) for j in range(start - 1, end + 1)]
            count = sum(
                0 <= x < len(lines) and 0 <= y < len(lines[x]) and lines[x][y] != "."
                for x, y in idxs
            )
            if count > 0:
                result += int(number)

print(result)


# part 2

result = 0

with open("input3.txt") as f:
    lines = f.read().splitlines()
    adj = defaultdict(list)
    for i, line in enumerate(lines):
        numbers = extract_numbers_and_indexes(line)
        for number, start, end in numbers:
            idxs = [(i, start - 1), (i, end)] 
            idxs += [(i - 1, j) for j in range(start - 1, end + 1)]
            idxs += [(i + 1, j) for j in range(start - 1, end + 1)]
            for x, y in idxs:
                if 0 <= x < len(lines) and 0 <= y < len(lines[x]) and lines[x][y] == "*":
                    adj[(x, y)].append(int(number))
    result = sum(int(x[0] * int(x[1])) for x in adj.values() if len(x) == 2)

print(result)
