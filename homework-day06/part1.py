import sys

def product(l: list):
    res = 1
    for a in l: res *= a
    return res

filename = "sample.txt"
if len(sys.argv) >= 2:
    filename = sys.argv[1]

lines = list(map(str.strip, open(filename, "r").readlines()))

numbers = [[] for _ in range(len(lines[0].split()))]

for line in lines[:-1]:
    nums = list(map(int, line.split()))
    for ind, num in enumerate(nums):
        numbers[ind].append(num)

sum_p1 = 0
for index, operation in enumerate(lines[-1].split()):
    op = None
    match operation:
        case '+': op = sum
        case '*': op = product
    sum_p1 += op(numbers[index])

print("Part 1 sum:")
print(sum_p1)