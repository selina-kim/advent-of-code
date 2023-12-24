############# Example Part 1 #############
EXAMPLE = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4""".strip()
##########################################

PUZZLE = ""

with open("puzzle-input/day5.txt", 'r') as fh:
    PUZZLE = fh.read().strip()

def solution(input):

    lines = input.split("\n")

    seeds = []

    for line_idx, line in enumerate(lines):

        # store original seeds
        if line_idx == 0:
            seeds = line.split(":")[1].strip().split(" ")
            
            for seed_idx, seed in enumerate(seeds):
                seeds[seed_idx] = int(seed)

        # map
        elif lines[line_idx-1][-4:] == "map:":
            # print(lines[line_idx-1])

            # keep track of which seeds are alr converted
            check = [False for _ in range(len(seeds))]

            # organize mapping
            i = line_idx
            while True:
                if (lines[i] != ""):
                    destStart = int(lines[i].split(" ")[0])
                    srcStart = int(lines[i].split(" ")[1])
                    rangeLen = int(lines[i].split(" ")[2])

                    # print("source:", srcStart, "~", srcStart+rangeLen)
                    # print("destination:", destStart, "~", destStart+rangeLen)

                    # print(seeds)

                    # update seeds
                    for seed_idx, seed in enumerate(seeds):
                        if (seed < srcStart+rangeLen) and (seed >= srcStart) and not check[seed_idx]:
                            seeds[seed_idx] = destStart + (seed - srcStart)
                            check[seed_idx] = True
                    
                    # print(seeds)

                    i += 1

                    if (i == len(lines)): break

                else: break

    print(seeds)
    print(min(seeds))

# solution(EXAMPLE)
solution(PUZZLE)