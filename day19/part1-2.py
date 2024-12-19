import sys
from functools import lru_cache

if len(sys.argv) >= 2:
    filename = sys.argv[1]
else:
    filename = "sample.txt"

data = open(filename).readlines()

towels = set(data[0].strip().split(", "))
patterns = list(map(str.strip, data[2:]))

def substring_set(string:str, start_index:int) -> set:
    res = set()
    for i in range(start_index, len(string) + 1):
        res.add(string[start_index:i])
    return res

@lru_cache
def count(string:str):
    res = 0
    subs = substring_set(string, 0)
    inter = subs.intersection(towels)
    if len(inter) == 0:
        return 0
    
    for intersection in inter:
        if intersection == string: res += 1
        res += count(string[len(intersection):])

    return res

possible_count = 0
ways_count = 0

for pattern in patterns:
    print(f"Pattern {pattern}")
    res = count(pattern)

    ways_count += res
    if res > 0: possible_count += 1

    print(f"    possible in {res} ways")

print("\nPart 1:", possible_count)
print("Part 2:", ways_count)
    