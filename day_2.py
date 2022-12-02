decodes = {"A": "Rock", "B": "Paper", "C": "Scissors"}
defeats = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}
shape_score = {"Rock": 1, "Paper": 2, "Scissors": 3}


def outcome_score(my_record, other_record):
    defeats = [["Rock", "Scissors"], ["Paper", "Rock"], ["Scissors", "Paper"]]
    if my_record == other_record:
        return 3
    elif [my_record, other_record] in defeats:
        return 6
    return 0


strategy = {"X": "Rock", "Y": "Paper", "Z": "Scissors"}
score = 0

with open("./data/advent2022/input2.txt", "r") as f:
    records = [s[:-1].split(" ") for s in f.readlines()]
    for i, (other, me) in enumerate(records):
        score += outcome_score(strategy[me], decodes[other])
        score += shape_score[strategy[me]]
print(score)

strategy = {"X": "lose", "Y": "draw", "Z": "win"}
score = 0
with open("./data/advent2022/input2.txt", "r") as f:
    records = [s[:-1].split(" ") for s in f.readlines()]
    for i, (other, me) in enumerate(records):
        if me == "X":
            shape = defeats[decodes[other]]
        elif me == "Y":
            score += 3
            shape = decodes[other]
        elif me == "Z":
            score += 6
            loses = {v: k for k, v in defeats.items()}
            shape = loses[decodes[other]]
        score += shape_score[shape]

print(score)
