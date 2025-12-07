import sys

filename = "sample.txt"
if len(sys.argv) >= 2:
    filename = sys.argv[1]

fresh_ids = set()
ids = []


with open(filename, "r") as file:
    while (line := file.readline().strip()) != "":
        (start, end) = tuple(map(int, line.split("-")))
        fresh_ids = fresh_ids.union(set(range(start, end+1)))
    print("range parsin fin")
    while line := file.readline().strip():
        ids.append(int(line))
    print("parsing fin")

total_fresh = len(fresh_ids.intersection(set(ids)))

print("Part 1 fresh ingredients:")
print(total_fresh)