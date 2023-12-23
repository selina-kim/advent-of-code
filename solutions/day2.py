bag = {
    "red": 12,
    "green": 13,
    "blue" : 14
}

res = 0
lines = []

with open("puzzle-input/day2.txt", 'r') as fh:
    s = fh.read().strip()
    lines = s.split("\n")

############# Example Part 2 #############
# x = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".strip()
# lines = x.split("\n")
##########################################

for line in lines:
    fewest = {
        "red": 0,
        "green": 0,
        "blue" : 0
    }
    # store game ID
    game_id = line.split(":")[0].strip("Game ")
    
    # remove "Game ??:" part and split up the rounds into a list
    game_data = line.split(":")[1].split(";")
    
    for round in game_data:
        cubes = round.split(",") # split up each cube colour
        
        for cube_count in cubes:
            for col in fewest: # go thru each colour
                if cube_count.endswith(col):
                    if (int(cube_count.split()[0]) > fewest[col]):
                        fewest[col] = int(cube_count.split()[0])
                        break

    # print(fewest)
    res += fewest["red"] * fewest["green"] * fewest["blue"]

print(res)