import sys

try:
    filename = sys.argv[1] + ".txt"
except IndexError:
    filename = "sample1.txt"

nums = open(filename).read().split()
nums = list(map(int, nums))

iterations = 75
#nums = [0]

def iter(number, iteration):
    #print(f"iteration {iteration}, stone {number}")
    if iteration == iterations: return 1

    if number == 0: return iter(1, iteration + 1)
    elif len(str(number)) % 2 == 0:
            string = str(number)
            length = int(len(string) / 2)
            first = int(string[:length])
            last = int(string[length:])
            
            return iter(first, iteration + 1) + iter(last, iteration + 1)
    else:
        return iter(number * 2024, iteration + 1)

length = 0#len(nums)

for i in range(len(nums)):
    print("Calculating stone", i)
    length += iter(nums[i], 0)

print("Stones:", length)