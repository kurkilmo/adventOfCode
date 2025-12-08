import sys
import itertools
import math

def distance(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)

def copy(l: list[set]):
    return [s.copy() for s in l]

filename = "sample.txt"
if len(sys.argv) >= 2:
    filename = sys.argv[1]

junctions = []


for line in open(filename, "r").readlines():
    junctions.append(tuple(map(int,line.strip().split(","))))

combs = list(itertools.combinations(range(len(junctions)), 2))

for i in range(len(combs)):
    a, b = combs[i]
    jA = junctions[a]
    jB = junctions[b]
    combs[i] = (a, b, distance(jA, jB))

combs.sort(key=lambda v: v[2])

junction_amt = 0
if filename == "sample.txt":
    junction_amt = 10
else:
    junction_amt = 1000

circuits: list[set] = list(map(lambda s: set(s[:-1]), combs[:junction_amt]))

for c in circuits:
    print(c)
print("...")
merged = True
while merged:
    merged = False
    for i1, cir1 in enumerate(copy(circuits)):
        for i2, cir2 in enumerate(copy(circuits)):
            if i1 == i2: continue

            if not cir1.isdisjoint(cir2):
                circuits.remove(cir1)
                circuits.remove(cir2)
                circuits.append(cir1.union(cir2))

                merged = True
                break
        if merged: break

circuits.sort(key=lambda c: -len(c))
print(circuits)
part1_product = 1
for circuit in circuits[:3]:
    part1_product *= len(circuit)

print("Part 1 product:")
print(part1_product)