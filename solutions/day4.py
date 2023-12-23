############# Example Part 1 #############
EXAMPLE = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".strip()
##########################################

PUZZLE = ""

with open("puzzle-input/day4.txt", 'r') as fh:
    PUZZLE = fh.read().strip()

def find_winning(lines):
    if len(lines) > 0:
        winning = lines[0].split(":")[1].split("|")[0].strip().split()
        mine = lines[0].split(":")[1].split("|")[1].strip().split()
        count = 0
        
        for num in mine:
            if num in winning:
                count +=1
        return count

def solution(input):

    lines = input.split("\n")
    res = [0 for _ in range(len(lines))]

    all_count = {}

    for line_idx, line in enumerate(lines):
        res[line_idx] += 1

        if line_idx not in all_count:
            all_count[line_idx] = find_winning(lines[line_idx:])

        if all_count[line_idx] > 0:
            for n in range(0, all_count[line_idx]):
                res[line_idx+n+1] += res[line_idx]
                all_count[line_idx+n+1] = find_winning(lines[line_idx+n+1:])

    # print(all_count)
    print(res, sum(res))

solution(PUZZLE)