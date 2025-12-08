import sys
import itertools
import math

def distance(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)

filename = "sample.txt"
if len(sys.argv) >= 2:
    filename = sys.argv[1]

junctions = [] # List of coordinate tuples (x,y,z)
for line in open(filename, "r").readlines():
    junctions.append(tuple(map(int,line.strip().split(","))))

# List of 2-combinations of junction indices
combs = list(itertools.combinations(range(len(junctions)), 2))

for i in range(len(combs)):
    a, b = combs[i]
    jA = junctions[a]
    jB = junctions[b]
    # Add distance infor to combinations
    combs[i] = (a, b, distance(jA, jB))

# Sort by distance
combs.sort(key=lambda v: v[2])

# How many junctions are processed for part 1
junction_amt = 0
if filename == "sample.txt":
    junction_amt = 10
else:
    junction_amt = 1000

# List of sets of junction indices
circuits: list[set] = []
def merge(index):
    circuits.append(set(combs[index][:-1]))
    merged = True
    while merged:
        merged = False
        for i1 in range(len(circuits)):
            for i2 in range(i1+1, len(circuits)):
                cir1 = circuits[i1]
                cir2 = circuits[i2]

                if not cir1.isdisjoint(cir2):
                    circuits.remove(cir1)
                    circuits.remove(cir2)
                    circuits.append(cir1.union(cir2))

                    merged = True
                    break
            if merged: break

p1_prod = 1
p2_prod = 0
for i in range(len(combs)):
    a, b, distance = combs[i]
    jA = junctions[a]
    jB = junctions[b]

    merge(i)

    # Part 1: if correct amount has been processed,
    # Get the product of three longest circuits
    if i == junction_amt-1:
        for circ in sorted(circuits, key=lambda c: -len(c))[:3]:
            p1_prod *= len(circ)

    print(f"{i=}, {jA=}, {jB=}, {len(circuits)} circuits")

    # Part 2: if only one circuit remains
    # and it contains all junctions, stop
    if len(circuits) == 1:
        if len(circuits[0]) == len(junctions):
            p2_prod = jA[0]*jB[0]
            break

print("Part 1:")
print(p1_prod)
print("Part 2:")
print(p2_prod)
