import sys

try:
    filename = sys.argv[1] + ".txt"
except IndexError:
    filename = "sample2.txt"

nums = open(filename).read().split()
nums = list(map(int, nums))

iterations = 75

stones = dict()

for num in nums:
    stones[num] = 1

def add(key, amount):
    try:
        stones[key] += amount
    except KeyError:
        stones[key] = amount

for it in range(iterations):
    keys = stones.copy().keys()
    stones_2 = stones.copy()
    for stone in keys:
        amount = stones_2[stone]
        stones[stone] -= amount
        if stone == 0:
            add(1, amount)
        elif len(str(stone)) % 2 == 0:
            string = str(stone)
            length = int(len(string) / 2)
            first = int(string[:length])
            last = int(string[length:])

            add(first, amount)
            add(last, amount)
        else:
            add(stone * 2024, amount)

amount = sum(stones.values())

print("Stones: ", amount)