from collections import defaultdict
import math

test = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""


test = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""

with open("input8.txt") as f:
    lines = f.read()


nav, network = lines.split("\n\n")
# nav, network = test.split("\n\n")


network = [node.split(" = ") for node in network.splitlines()]
nodes = {}
for node, links in network:
    choices = links.split(", ")
    nodes[node] = (choices[0][1:], choices[1][:-1])

found = False

node = "AAA"
step = 0

while not found:
    for direction in nav:
        if direction == "L":
            node = nodes[node][0]
        else:
            node = nodes[node][1]
        step += 1
        if node == "ZZZ":
            found = True
            break
print(step)

print("-----------------------")

test = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""

## part 2

start_nodes = []

# nav, network = test.split("\n\n")
nav, network = lines.split("\n\n")

network = [node.split(" = ") for node in network.splitlines()]
nodes = {}
for node, links in network:
    choices = links.split(", ")
    nodes[node] = (choices[0][1:], choices[1][:-1])
    if node.endswith("A"):
        start_nodes.append(node)

steps = {idx: [False, 0] for idx, _ in enumerate(start_nodes)}

found = False
while not found:
    for direction in nav:
        for i, node in enumerate(start_nodes):
            if direction == "L":
                start_nodes[i] = nodes[node][0]
            else:
                start_nodes[i] = nodes[node][1]
            if not steps[i][0]:
                steps[i][1] += 1
            if start_nodes[i].endswith("Z"):
                steps[i][0] = True
            if all([f for f, _ in steps.values()]):
                found = True
                break
            

print(math.lcm(*[x[1] for x in steps.values()]))