lines = []

with open("puzzle-input/day1.txt", 'r') as fh:
    s = fh.read().strip()
    lines = s.split("\n")

############# Example Part 1 #############
# x = """1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet""".strip()
# lines = x.split("\n")
##########################################

############# Example Part 2 #############
# x = """two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen""".strip()
# lines = x.split("\n")
##########################################

# converting digits from word -> number
nums = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

allNums = []

for line in lines:
    fst = None
    lst = None

    # find first digit
    for i, char in enumerate(line):
        
        if char.isdigit():
            fst = char
            break
            
        else:
            for key in nums:
                if line[:i+1].endswith(key):
                    fst = nums[key]
                    break
                    
        if fst != None:
            break
        
    # find last digit
    for i, char in reversed(list(enumerate(line))):
        if char.isdigit():
            lst = char
            break
            
        else:
            for key in nums:
                if line[i:].startswith(key):
                    lst = nums[key]
                    break
                    
        if lst != None:
            break

    fullNum = int(fst + lst)
    print(line, fullNum)
    allNums.append(fullNum)

# print(allNums)

# print answer
print("\nanswer: " + str(sum(allNums)))