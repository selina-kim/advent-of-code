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

    times = [int(n) for n in lines[0].split(":")[1].strip().split()]
    dists = [int(n) for n in lines[1].split(":")[1].strip().split()]
    ways = [0 for _ in range(len(times))]
    # ic(times)
    # ic(dists)

    for i in range(len(times)):
        t = times[i]
        passed = False
        for speed in range(times[i]+1):
            duration = t - speed
            # ic(t, speed, duration)
            if (speed * duration) > dists[i]:
                if not passed:
                    passed = True
                ways[i] += 1
                # ic("works !", speed * duration, dists[i])
            elif passed:
                break

    ic(ways)
    res = 1

    for n in ways:
        res *= n

    print(res)

# solution(EXAMPLE)
solution(PUZZLE)