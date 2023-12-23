lines = []
res = []

with open("puzzle-input/day3.txt", 'r') as fh:
    s = fh.read().strip()
    lines = s.split("\n")

############# Example Part 1 #############
# x = """467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..""".strip()
# lines = x.split("\n")
##########################################

def is_symbol(string):
    if string != "." and not string.isdigit():
        return True
    return False

for idx, line in enumerate(lines):

    for char_idx, char in enumerate(line):
        num_len = 1
        # print('''"''' + str(char) + '''"''')
        if char.isdigit():

            is_part_num = False

            # if the prev character is a number (we alr checked so move on)
            if char_idx !=0 and line[char_idx-1].isdigit():
                continue
            # first check how long this number is
            for x in range(char_idx+1, len(line)):
                if line[x].isdigit():
                    num_len += 1
                else: break
                
            for i in range(char_idx, char_idx+num_len):
                # first digit of num
                if i == char_idx and i != 0:
                    # check same line (left)
                    if is_symbol(line[i-1]):
                        is_part_num = True
                        break
                    # check prev line (left up diagonal)
                    if idx != 0:
                        if is_symbol(lines[idx-1][i-1]):
                            is_part_num = True
                            break
                    # check next line (left down diagonal)
                    if idx != len(lines)-1:
                        if is_symbol(lines[idx+1][i-1]):
                            is_part_num = True
                            break
                # last digit of num
                if i == char_idx+num_len-1 and i != len(line)-1:
                    # check same line (right)
                    if is_symbol(line[i+1]):
                        is_part_num = True
                        break
                    # check prev line (right up diagonal)
                    if idx != 0:
                        if is_symbol(lines[idx-1][i+1]):
                            is_part_num = True
                            break
                    # check next line (right down diagonal)
                    if idx != len(lines)-1:
                        if is_symbol(lines[idx+1][i+1]):
                            is_part_num = True
                            break
                # middle digits
                # check prev line (up)
                if idx != 0:
                    if is_symbol(lines[idx-1][i]):
                        is_part_num = True
                        break
                # check next line (down)
                if idx != len(lines)-1:
                    if is_symbol(lines[idx+1][i]):
                        is_part_num = True
                        break
            
            if is_part_num:
                res.append(int(line[char_idx:char_idx+num_len]))
                    
print(res, "\n", sum(res))