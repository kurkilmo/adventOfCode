import sys

if len(sys.argv) >= 2:
    filename = f"{sys.argv[1]}.txt"
else:
    filename = "input.txt"

lines = open(filename).readlines()

safes = 0

def norm(num):
    if num == 0: return num
    return num / abs(num)

def permutate(lst: list):
    res = []
    for i in range(len(lst)):
        ls = lst.copy()
        ls.pop(i)
        res.append(ls)
    return res

for line in lines:
    nums = list(map(int, line.split()))
    permutations = permutate(nums)
    for perm in permutations:
        stop = False
        first_diff = perm[0] - perm[1]
        if abs(first_diff) > 3: continue
        for i in range(2, len(perm)):
            diff = perm[i-1] - perm[i]
            if abs(diff) > 3 or diff == 0: break
            if norm(diff) != norm(first_diff): break

            if i == len(perm) - 1:
                safes += 1
                stop = True
        if stop: break
            

print("Part 2:", safes)
