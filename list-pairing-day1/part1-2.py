lines = open("input.txt").readlines()

left = []
right = []
for line in lines:
    spl = line.split(" ")
    left.append(int(spl[0]))
    right.append(int(spl[-1]))

left.sort()
right.sort()

# Part 1
sum_part1 = 0
for i in range(len(left)):
    sum_part1 += abs(left[i] - right[i])

print("Part 1:", sum_part1)

# Part 2
sum_part2 = 0
for num in left:
    sum_part2 += num * right.count(num)

print("Part 2:", sum_part2)