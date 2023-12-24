from icecream import ic

############# Example Part 1 #############
EXAMPLE = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)""".strip()
##########################################

PUZZLE = ""

with open("puzzle-input/day8.txt", 'r') as fh:
    PUZZLE = fh.read().strip()

def solution(input):

    lines = input.split("\n")

    instructions = ""
    network = {}

    # store ---------------------
    for line_idx, line in enumerate(lines):
        if line_idx == 0:
            instructions = line
            # ic(instructions)
        elif line != "":
            network[line.split(" = ")[0]] = line.split(" = ")[1].strip("()").split(", ")
    
    # ic(network)

    found = False
    res = 0
    curr = "AAA"

    # go thru network

    while True:
        
        for char in instructions:
            # ic(elems[curr])
            # ic(char)
            # ic(res)
            if curr == "ZZZ":
                print("found!")
                found = True
                break

            res += 1

            if char == "L":
                curr = network[curr][0]
            else:
                curr = network[curr][1]

        if found: break
    
    ic(res)

# solution(EXAMPLE)
solution(PUZZLE)