def get_first_and_last_digit(s):
    result = []
    for _, c in enumerate(s):
        if c.isdigit():
            result.append(int(c))
    return result


total = 0

for line in open("input1.txt"):
    numbers = get_first_and_last_digit(line.strip())
    total += numbers[0] * 10 + numbers[-1]
print(total)

# part two

print("--------------------")
dic = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def get_numbers_only(s):
    result = []
    for i, c in enumerate(s):
        if c.isdigit():
            result.append(int(c))
        else:
            for number in dic:
                if s[i : i + len(number)] == number:
                    result.append(dic[number])
    return result


total = 0
for line in open("input1.txt"):
    line = line.strip()
    numbers = get_numbers_only(line)
    total += numbers[0] * 10 + numbers[-1]
print(total)
