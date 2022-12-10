from utils import parse


def day10_1():
    data = parse(10)

    cycles, x, strength = 0, 1, 0
    for line in data:
        if line == "noop":
            cycles += 1
            if cycles in [20, 60, 100, 140, 180, 220]:
                strength += cycles * x
        else:
            _, num = line.split(" ")
            for _ in range(2):
                cycles += 1
                if cycles in [20, 60, 100, 140, 180, 220]:
                    strength += cycles * x

            x += int(num)

    return strength


print(day10_1())


def day10_2():
    data = parse(10)

    pixel = "#"
    sprite = [["."] * 40 for _ in range(6)]

    cycles, x = 0, 1
    for line in data:
        if line == "noop":
            if cycles % 40 in [x - 1, x, x + 1]:
                r = cycles // 40
                c = cycles % 40
                sprite[r][c] = pixel
            cycles += 1
        else:
            _, num = line.split(" ")
            for _ in range(2):
                if cycles % 40 in [x - 1, x, x + 1]:
                    r = cycles // 40
                    c = cycles % 40
                    sprite[r][c] = pixel
                cycles += 1
            x += int(num)

    for row in sprite:
        print("".join(row))

    return


day10_2()
