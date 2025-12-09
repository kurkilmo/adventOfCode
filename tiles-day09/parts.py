import sys
import itertools
import math

def area(a, b):
    offs_x = 0
    if b[0] >= a[0]:
        offs_x = 1
    else:
        offs_x = -1
    offs_y = 0
    if b[1] >= a[1]:
        offs_y = 1
    else:
        offs_y = -1
    return abs(a[0]-(b[0]+offs_x)) * abs(a[1]+-(b[1]+offs_y))

filename = "sample.txt"
if len(sys.argv) >= 2:
    filename = sys.argv[1]

tiles = [] # List of coordinate tuples (x,y,z)
for line in open(filename, "r").readlines():
    tiles.append(tuple(map(int,line.strip().split(","))))


# List of 2-combinations of tile pairs
combs = list(itertools.combinations(range(len(tiles)), 2))

for i in range(len(combs)):
    a, b = combs[i]
    jA = tiles[a]
    jB = tiles[b]
    # Add area info to combinations
    combs[i] = (a, b, area(jA, jB))

# Sort by area
combs.sort(key=lambda v: v[2])

#tests=[[(2,5),(9,7)], [(7,1),(11,7)], [(7,3),(2,3)], [(2,5),(11,1)]]
#
#for c in combs:
#    for test in tests:
#        if tiles[c[0]] in test and tiles[c[1]] in test:
#            print(f"{tiles[c[0]]}-{tiles[c[1]]}: {c[2]}")
#            print()


print("Part 1 largest area:")
print(combs[-1][-1])