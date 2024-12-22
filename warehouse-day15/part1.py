import sys
import time

if len(sys.argv) >= 2:
    filename = sys.argv[1]
else:
    filename = "sample.txt"

data = open(filename).readlines()

boxes = []
robot = ()

i = 0
while data[i] != "\n":
    for j in range(len(data[i])):
        coord = (i, j)
        match data[i][j]:
            case '@':
                robot = coord
            case 'O':
                boxes.append(coord)
    i += 1
size = i

route = []
for ii in range(i, len(data)):
    route += list(data[ii].strip())
route = list(map(lambda d: ['^','>','v','<'].index(d), route))

def insert_string(s: str):
    lines = s.split('\n')
    #lines.reverse()
    sys.stdout.write('\33[A' * (len(lines)))
    for line in lines:
        sys.stdout.write(line + '\n')
    sys.stdout.flush()

def visual(direction):
    res = ""
    for i in range(size):
        line = ""
        for j in range(size):
            c = (i,j)
            if data[i][j] == "#":
                line += "#"
            elif c == robot:
                line += "@"
            elif c in boxes:
                line += "O"
            else:
                line += "."
        res += line + "\n"
    res += ['^','>','v','<'][direction]
    return res

def next_square(direction, square):
    return (
        square[0] + (-1*abs(direction-2)+1),
        square[1] + (-1*abs(direction-1)+1)
    )

def is_wall(square):
    return data[square[0]][square[1]] == "#"

print(visual(0))

for direction in route:
    insert_string(visual(direction))
    time.sleep(0.05)

    next = next_square(direction, robot)

    if is_wall(next):
        continue

    if next not in boxes:
        robot = next
        continue
    
    pointer = next
    move = True
    while pointer in boxes or is_wall(pointer):
        if is_wall(pointer):
            move = False
            break
        pointer = next_square(direction, pointer)

    if not move: continue

    prev_direction = (direction + 2) % 4
    boxes.append(pointer)
    while next_square(prev_direction, pointer) != robot:
        pointer = next_square(prev_direction, pointer)
    boxes.remove(pointer)
    robot = pointer

insert_string(visual(direction))

coords = 0
for box in boxes:
    coords += box[0] * 100 + box[1]

print(f"Part 1:\n{coords}")