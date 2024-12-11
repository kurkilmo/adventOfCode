import sys

try:
    filename = sys.argv[1] + ".txt"
except IndexError:
    filename = "input.txt"

nums = open(filename).read().split()
nums = list(map(int, nums))

iterations = 25

for it in range(iterations):
    i = 0
    print("Iteration", it)
    while i < len(nums):
        if nums[i] == 0: nums[i] = 1
        elif len(str(nums[i])) % 2 == 0:
            string = str(nums[i])
            length = int(len(string) / 2)
            first = string[:length]
            last = string[length:]
            
            nums.insert(i, int(first))
            i += 1
            nums[i] = int(last)
        else:
            nums[i] *= 2024
        i += 1
    #print(f"iteration {it}: {" ".join(list(map(str, nums)))}")

print("Part 1:", len(nums))