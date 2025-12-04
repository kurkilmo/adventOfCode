import sys
import time

def remove_lines(amount:int):
    #LINE_UP = '\033[1A'
    #LINE_CLEAR = '\x1b[2K'
    s = ('\33[A') * amount
    sys.stdout.write(s)

filename = "input.txt"
if len(sys.argv) >= 2:
    filename = sys.argv[1]

rolls = []
lines = open(filename).readlines()

for line in lines:
    row = []
    for char in line.strip():
        if char == "@": row.append(1)
        elif char == ".": row.append(0)
        else: raise ValueError
    rolls.append(row)


# Part 1: initially accessible rows
accessible = 0
accessible_inds = []
for y in range(len(rolls)):
    for x in range(len(rolls[y])):
        if not rolls[y][x]:
            print(".", end="")
            continue
        neighbors = 0
        for j in range(-1,2):
            for i in range(-1,2):
                if i == 0 and j == 0: continue
                if y+j < 0 or x+i < 0: continue
                try:
                    neighbors += rolls[y+j][x+i]
                except IndexError: continue
        if neighbors < 4:
            accessible += 1
            accessible_inds.append((y,x))
            print("X", end="")
        else:
            print("@", end="")
    print()

print("Part 1 accessible rolls:")
print(accessible)

# Part 2: removing accessible rolls
start = True
removed = 0
removed_inds = []
while len(removed_inds) != 0 or start:
    if not start:
        remove_lines(len(rolls))
    start = False
    removed_inds = []
    for y in range(len(rolls)):
        for x in range(len(rolls[y])):
            if not rolls[y][x]:
                print(".", end="")
                continue
            neighbors = 0
            for j in range(-1,2):
                for i in range(-1,2):
                    if i == 0 and j == 0: continue
                    if y+j < 0 or x+i < 0: continue
                    try:
                        neighbors += rolls[y+j][x+i]
                    except IndexError: continue
            if neighbors < 4:
                removed_inds.append((y,x))
                print("X", end="")
            else:
                print("@", end="")
        print()
    
    for (y, x) in removed_inds:
        rolls[y][x] = 0
    removed += len(removed_inds)


print("Part 1 removed rolls:")
print(removed)