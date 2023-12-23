lines = []

with open("./puzzle-input/day1.txt", 'r') as fh:
    s = fh.read().strip()
    lines = s.split("\n")

############# Example Part 1 #############
# x = """1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet""".strip()
# lines = x.split("\n")
##########################################

allNums = []

for line in lines:
    fst = None
    lst = None

    # find first digit
    for i, char in enumerate(line):
        
        if char.isdigit():
            fst = char
            break
                    
        if fst != None:
            break
        
    # find last digit
    for i, char in reversed(list(enumerate(line))):
        if char.isdigit():
            lst = char
            break

        if lst != None:
            break

    fullNum = int(fst + lst)
    print(line, fullNum)
    allNums.append(fullNum)

# print(allNums)

# print answer
print("\nanswer: " + str(sum(allNums)))