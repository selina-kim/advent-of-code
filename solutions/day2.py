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

for line in lines:
    # store game ID
    game_id = line.split(":")[0].strip("Game ")
    
    # remove "Game ??:" part and split up the rounds into a list
    game_data = line.split(":")[1].split(";")

    possible = True
    
    for round in game_data:
        cubes = round.split(",") # split up each cube colour
        
        for cube_count in cubes:
            for key in bag: # go thru each colour
                if cube_count.endswith(key):
                    if (int(cube_count.split()[0]) > bag[key]):
                        possible = False
                        break
                        
            if not possible:
                break


        if not possible:
            break

    if possible:
        res += int(game_id)

print(res)