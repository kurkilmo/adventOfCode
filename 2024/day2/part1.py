lines = open("input.txt").readlines()

safes = 0

def norm(num):
    if num == 0: return num
    return num / abs(num)

for line in lines:
    nums = list(map(int, line.split()))
    first_diff = nums[0] - nums[1]
    if abs(first_diff) > 3: continue
    for i in range(2, len(nums)):
        diff = nums[i-1] - nums[i]
        if abs(diff) > 3 or diff == 0: break
        if norm(diff) != norm(first_diff): break

        if i == len(nums) - 1: safes += 1

print("Part 1:", safes)
