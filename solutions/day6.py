from icecream import ic

############# Example Part 1 #############
EXAMPLE = """Time:      7  15   30
Distance:  9  40  200""".strip()
##########################################

PUZZLE = ""

with open("puzzle-input/day6.txt", 'r') as fh:
    PUZZLE = fh.read().strip()

def solution(input):

    lines = input.split("\n")

    res = None

    time = int(lines[0].split(":")[1].strip().replace(" ", ""))
    dist = int(lines[1].split(":")[1].strip().replace(" ", ""))

    ic(time)
    ic(dist)

    res = None

    for speed in range(time):
        duration = time - speed
        if speed * duration > dist:
            res = time - speed - speed + 1
            break

    print(res)

# solution(EXAMPLE)
solution(PUZZLE)