import sys

sys.setrecursionlimit(5000)

if len(sys.argv) >= 2:
    filename = sys.argv[1]
else:
    filename = "sample.txt"

pairs = list(map(
    lambda line: tuple(map(int,line.split(","))),
    open(filename).readlines()
))

fall_amount = 12
if filename == "input.txt": fall_amount = 1024

fallen = pairs[:fall_amount]

size = max(map(max, pairs))

grid = [[0] * (size+1) for _ in range(size+1)]
visited = dict()

def neighbors(i, j):
    return list(filter(
        lambda c: c[0] in range(size+1) and c[1] in range(size+1),
        [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]
    ))

end_distances = []

def visit(distance, i, j):
    #print(f"visiting {i} {j}")
    if (j,i) in fallen:
        #print("fallen")
        return
    if distance in end_distances: return
    if (i,j) in visited.keys():
        if visited[(i,j)] <= distance:
            return
    #print("continuing")
    visited[(i,j)] = distance
    grid[i][j] = distance
    if i == size and j == size:
        print("End:", distance)
        end_distances.append(distance)
        return
    for c in neighbors(i, j):
        visit(distance+1, c[0], c[1])

#visit(0, 0, 0)
for i in range(size+1):
    line = ""
    for j in range(size+1):
        if (j,i) in fallen:
            line += "xx "
            continue
        if grid[i][j] == 0:
            line += ".. "
        else:
            line += str(grid[i][j]).zfill(2) + " "
    #print(line)
#print("\nMinumun distance:", min(end_distances))

# Part 2
visited = dict()
cont = True
def visit_part2(distance, i, j):
    global cont
    if not cont: return 0
    if (j,i) in fallen:
        return 0
    if (i,j) in visited.keys():
        if visited[(i,j)] <= distance:
            return 0
    #print("continuing")
    visited[(i,j)] = distance
    if i == size and j == size:
        cont = False
        return 1
    sum = 0
    for c in neighbors(i, j):
        sum += visit_part2(distance + 1, c[0], c[1])
    return sum

for i in range(1024, len(pairs)):
    pair = pairs[i]
    fallen = pairs[:i+1]
    cont = True
    visited = dict()
    res = visit_part2(0,0,0)
    if res == 0:
        print(f"Final pair: {fallen[-1]} (n.{i})")
        break
    else:
        print(f"{fallen[-1]} okay (n.{i})")
