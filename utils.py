from typing import List


def data(day: int, parser=str, sep="\n") -> List:
    "split the day's input file into sections seperated by `sep`, and apply `parser` to each."
    with open(f"data/advent2022/input{day}.txt", "r") as f:
        sections = f.read().rstrip().split(sep)
        return list(map(parser, sections))
