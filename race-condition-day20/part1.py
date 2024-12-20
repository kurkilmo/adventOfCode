import sys

if len(sys.argv) >= 2:
    filename = sys.argv[1]
else:
    filename = "sample.txt"

sys.setrecursionlimit(10000)

data = open(filename).readlines()
size = len(data)

start = ()
end = ()

for i in range(size):
    for j in range(size):
        coord = (i, j)
        match data[i][j]:
            case 'S':
                start = coord
            case 'E':
                end = coord

def neighbors(pos):
    (i,j) = pos
    res =  [
        (i-1, j),
        (i, j-1),
        (i+1, j),
        (i, j+1)
    ]
    return list(filter(
        lambda d: d[0] in range(size) and d[1] in range(size),
        res
    ))

route = dict()
def traverse(distance, pos):
    if pos in route.keys():
        if route[pos] < (distance): return 0

    route[pos] = distance
    if pos == end:
        return distance

    res = 0

    for n in neighbors(pos):
        if data[n[0]][n[1]] != '#':
            res += traverse(distance+1, n)

    return res

end_distance = traverse(0,start)

def double_neighbors(i, j):
    res =  [
        [(i-1, j) , (i-2, j)],
        [(i, j-1) , (i, j-2)],
        [(i+1, j) , (i+2, j)],
        [(i, j+1) , (i, j+2)],
    ]
    return list(filter(
        lambda d: d[0][0] in range(size) and d[0][1] in range(size) and d[1][0] in range(size) and d[1][1] in range(size),
        res
    ))

# Part 1
cheats = []
cheat_locs = []
for spot in route.keys():
    (i,j) = spot
    for d in double_neighbors(i, j):
        first = d[0]
        second = d[1]
        if data[first[0]][first[1]] == "#" and second in route.keys():
            if route[second] > route[spot]:
                cheats.append((route[second] - route[spot]) - 2)
                cheat_locs.append(first)

if filename != "input.txt":
    for i in range(size):
        line = ""
        for j in range(size):
            if (i, j) in cheat_locs:
                line += "-----"
            elif data[i][j] == "#":
                line += "#===#"
            elif data[i][j] == "S":
                line += "  S  "
            elif (i,j) in route.keys():
                line += f"[{str(route[(i,j)]).zfill(3)}]"
            else:
                line += "     "
        print(line)

cheat_threshold = 100
fast_cheats = len(list(filter(lambda c: c >= cheat_threshold, cheats)))

print(f"Part 1:\nDistance w/o cheats: {end_distance}")
print(f"\nTotal cheats: {len(cheats)}\n")

if filename != "input.txt":
    for cheat in set(cheats):
        print(f"{cheats.count(cheat)} cheats saving {cheat} ps")

print(f"\nCheats saving {cheat_threshold}ps or more:")
print(fast_cheats)

# Part 2
print("-----------\nPart 2:")
def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

cheat_dist = 20
cheats = []
for spot in route.keys():
    for cheat_spot in list(filter(
        lambda s: distance(spot, s) <= cheat_dist,
        route.keys()
    )):
        if route[cheat_spot] > route[spot]:
            cheats.append((route[cheat_spot] - route[spot]) - distance(cheat_spot, spot))


cheat_threshold = 100
fast_cheats = len(list(filter(lambda c: c >= cheat_threshold, cheats)))

if filename != "input.txt":
    for cheat in set(cheats):
        if cheat >= cheat_threshold:
            print(f"{cheats.count(cheat)} cheats saving {cheat} ps")

print(f"\nCheats saving {cheat_threshold}ps or more:")
print(fast_cheats)