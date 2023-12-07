
from collections import Counter
from functools import cmp_to_key
from itertools import product



s = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

# always good to learn from the best
# https://github.com/oliver-ni/advent-of-code/blob/master/py/2023/day07.py


def get_score(x):
    match [b for _, b in Counter(x).most_common()]:
        case 5, *_:
            return 1
        case 4, *_:
            return 2
        case 3, 2, *_:
            return 3
        case 3, *_:
            return 4
        case 2, 2, *_:
            return 5
        case 2, *_:
            return 6
        case _:
            return 7

# part 1

cards = {c: i for i, c in enumerate('23456789TJQKA')}
# print(cards)

def hand_rank(s):
    counter = Counter(s)
    if 5 in counter.values():
        return 5
    elif 4 in counter.values():
        return 4
    elif 3 in counter.values() and 2 in counter.values():
        return 3.5
    elif 3 in counter.values() and 2 not in counter.values():
        return 3
    elif list(counter.values()).count(2) == 2:
        return 2.5
    elif list(counter.values()).count(2) == 1:
        return 2
    else:
        return 1

def compare_hands(h1, h2):
    score1 = hand_rank(h1)
    score2 = hand_rank(h2)
    if score1 > score2:
        return 1
    elif score1 < score2:
        return -1
    else:
        for c1, c2 in zip(h1, h2):
            if cards[c1] > cards[c2]:
                return 1
            elif cards[c1] < cards[c2]:
                return -1

print(compare_hands("T55J5", "QQQJA"))
print(compare_hands("77788", "77888"))


lines = s.splitlines()

with open("input7.txt") as f:
    lines = f.read().splitlines()

hands = []
for line in lines:
    hand, bid = line.split()
    hands.append((hand, bid))

hands = sorted(hands, key=cmp_to_key(lambda x, y: compare_hands(x[0], y[0])))

res = 0
for i, (hand, bid) in enumerate(hands):
    res += (i + 1) * int(bid)

print(res)


# part 2


cards = {c: i for i, c in enumerate('J23456789TQKA')}

def new_hand_rank(hand):
    rank = hand_rank(hand)
    if "J" not in hand:
        return rank
    for replacement in product("23456789TQKA", repeat=hand.count("J")):
        rank = max(rank, hand_rank(hand.replace("J", "") + "".join(replacement)))
        
    return rank




def compare_hands(h1, h2):
    score1 = new_hand_rank(h1)
    score2 = new_hand_rank(h2)
    if score1 > score2:
        return 1
    elif score1 < score2:
        return -1
    else:
        for c1, c2 in zip(h1, h2):
            if c1 == c2:
                continue
            if cards[c1] > cards[c2]:
                return 1
            elif cards[c1] < cards[c2]:
                return -1

print(new_hand_rank("JKKK2"))
print(new_hand_rank("QQQQ2"))
print(compare_hands("JKKK2", "QQQQ2") == -1)

hands = []
for line in lines:
    hand, bid = line.split()
    hands.append((hand, bid))


hands = sorted(hands, key=cmp_to_key(lambda x, y: compare_hands(x[0], y[0])))

res = 0
for i, (hand, bid) in enumerate(hands):
    res += (i + 1) * int(bid)

print(res)

