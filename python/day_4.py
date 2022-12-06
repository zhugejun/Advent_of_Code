from utils import parse


def include(interval1, interval2):
    left1, right1 = interval1
    left2, right2 = interval2
    return (left1 >= left2 and right1 <= right2) or (
        left1 <= left2 and right1 >= right2
    )


def is_include(left1: int, right1: int, left2: int, right2: int) -> bool:
    return (left1 >= left2 and right1 <= right2) or (
        left1 <= left2 and right1 >= right2
    )


def is_overlap(left1: int, right1: int, left2: int, right2: int) -> bool:
    return not (left2 > right1 or left1 > right2)


def day4_1():
    data = parse(4)
    res = 0
    for assignments in data:
        assignment1, assignment2 = assignments.split(",")
        left1, right1 = assignment1.split("-")
        left2, right2 = assignment2.split("-")
        if is_include(int(left1), int(right1), int(left2), int(right2)):
            res += 1
    return res


print(day4_1())


def day4_2():
    data = parse(4)
    res = 0
    for assignments in data:
        assignment1, assignment2 = assignments.split(",")
        left1, right1 = assignment1.split("-")
        left2, right2 = assignment2.split("-")
        if is_overlap(int(left1), int(right1), int(left2), int(right2)):
            res += 1
    return res


print(day4_2())


# print(is_overlap(5, 6, 7, 9))
# print(is_overlap(10, 15, 7, 9))
