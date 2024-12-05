import re

data = open("input.txt").read()

def multiply(match):
    nums = re.findall("[0-9]+", match)
    return int(nums[0]) * int(nums[1])

#   Part 1
def find_muls_and_sum(string):
    muls = re.findall("mul\([0-9]+,[0-9]+\)", string)
    return sum(map(multiply, muls))

print("Part 1:", find_muls_and_sum(data))

# Part 2
dos = ""

def is_do(ind: int) -> bool:
    return data[ind:ind+4] == "do()"

def is_dont(ind: int) -> bool:
    return data[ind:ind+7] == "don't()"

do = True
for i in range(len(data)):
    if do:
        do = not is_dont(i)
    else:
        do = is_do(i)
    
    if do:
        dos += data[i]

print("Part 2:", find_muls_and_sum(dos))
