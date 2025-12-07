import sys

def product(l: list):
    res = 1
    for a in l: res *= a
    return res

ops = {
    '+': sum,
    '*': product
}

filename = "sample.txt"
if len(sys.argv) >= 2:
    filename = sys.argv[1]

lines = list(map(lambda a:a.replace('\n',''), open(filename, "r").readlines()))

numbers = [[] for _ in range(len(lines[-1].split()))]
num_ind = -1
for i in range(len(lines[0])):
    if lines[-1][i] in ops.keys():
        num_ind += 1
    number = ""
    for ni in range(len(lines)-1):
        number += lines[ni][i]
    numbers[num_ind].append(number)

sum_p2 = 0
for index, op in enumerate(lines[-1].split()):
    nums = list(map(int,
        filter(
            lambda s: s.strip()!="", 
            numbers[index]
    )))
    sum_p2 += ops[op](nums)

print("Part 2 sum:")
print(sum_p2)
