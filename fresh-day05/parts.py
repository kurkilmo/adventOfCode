import sys

filename = "sample.txt"
if len(sys.argv) >= 2:
    filename = sys.argv[1]

fresh_ranges = []
total_fresh = 0

def in_range(n: int, rang: list | tuple):
    return n >= rang[0] and n <= rang[1]


with open(filename, "r") as file:
    while (line := file.readline().strip()) != "":
        (start, end) = tuple(map(int, line.split("-")))
        fresh_ranges.append([start, end])

    while line := file.readline().strip():
        ID = int(line)
        for id_range in fresh_ranges:
            if ID >= id_range[0] and ID <= id_range[1]:
                total_fresh += 1
                break


print("Part 1 fresh ingredients:")
print(total_fresh)
overlapped = True

while overlapped:
    overlapped = False
    for ind1, rng in enumerate(fresh_ranges):
        for ind2, rng2 in enumerate(fresh_ranges):
            if ind2 == ind1: continue
            #if rng == rng2: continue

            if (rng[0] <= rng2[1]) and (rng[1] >= rng2[0]):
                fresh_ranges[ind2][0] = min(rng[0], rng2[0])
                fresh_ranges[ind2][1] = max(rng[1], rng2[1])

                fresh_ranges.pop(ind1)
                overlapped = True
                break
        if overlapped: break


total_fresh_ids = 0
for ranke in fresh_ranges:
    total_fresh_ids += ranke[1] - ranke[0] + 1

print("Part 2 fresh ids:")
print(total_fresh_ids)
