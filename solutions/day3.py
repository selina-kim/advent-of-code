############# Example Part 1 #############
EXAMPLE = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".strip()
##########################################

PUZZLE = ""

with open("puzzle-input/day3.txt", 'r') as fh:
    PUZZLE = fh.read().strip()

def is_symbol(string):
    if string != "." and not string.isdigit():
        return True
    return False

def find_num(line, idx):

    nums = []

    if line[idx].isdigit():
        start = idx
        end = idx
        # check left
        for i in range(idx, -1, -1):
            if line[i].isdigit():
                start = i
            else: break
        # check right
        for i in range(idx+1, len(line)):
            if line[i].isdigit():
                end = i
            else: break
        nums.append(int(line[start:end+1]))

    else:
        # check left
        if idx > 0:
            if line[idx-1].isdigit():
                num_len = 1
                for i in range(idx-2, -1, -1):
                    if line[i].isdigit():
                        num_len += 1
                    else: break
                nums.append(int(line[idx-num_len:idx]))
        # check right
        if idx < len(line)-1:
            if line[idx+1].isdigit():
                num_len = 1
                for i in range(idx+2, len(line)):
                    if line[i].isdigit():
                        num_len += 1
                    else: break
                nums.append(int(line[idx+1:idx+1+num_len]))
    
    return nums

def solution(input):

    lines = input.split("\n")
    res = []

    for line_idx, line in enumerate(lines):
        for char_idx, char in enumerate(line):
            # print('''"''' + str(char) + '''"''')

            if char == "*":

                part_nums = []

                # check prev line (up)
                if line_idx != 0:
                    part_nums.extend(find_num(lines[line_idx-1], char_idx))

                # check same line
                part_nums.extend(find_num(line, char_idx))
                
                # check next line (down)
                if line_idx != len(lines)-1:
                    part_nums.extend(find_num(lines[line_idx+1], char_idx))

                if len(part_nums) == 2:
                    res.append(part_nums[0] * part_nums[1])
                    
    print(res, "\n", sum(res))

solution(PUZZLE)