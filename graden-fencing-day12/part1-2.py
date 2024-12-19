import sys

try:
    filename = sys.argv[1] + ".txt"
except IndexError:
    filename = "sample.txt"

grid = open(filename).readlines()
for i in range(len(grid)):
    grid[i] = list(grid[i])

size = len(grid)
num_grid = [[0 for _ in range(size)] for _ in range(size)]

def check_coord(i, j):
    return i in range(size) and j in range(size)

# Change grid to indices istead of letters to handle separate regions
def change(i, j, index):
    char = grid[i][j]
    if char == '-': return
    grid[i][j] = '-'
    num_grid[i][j] = index
    for (ii, jj) in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
        if (check_coord(ii, jj)) and grid[ii][jj] == char:
            change(ii,jj,index)

index = 1
for i in range(size):
    for j in range(size):
        char = grid[i][j]
        if grid[i][j] != '-':
            change(i,j, index)
            index += 1

plots = dict()
# "G": [area , [per1, per2, per3]]

def add(char, perimeter):
    try:
        plots[char][0] += 1
        plots[char][1] += perimeter
    except KeyError:
        plots[char] = [1, perimeter]

# Iterate over grid of indices
for i in range(size):
    for j in range(size):
        perimeter = []
        index = num_grid[i][j]
        for (ii, jj) in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if (not check_coord(ii, jj)) or num_grid[ii][jj] != index:
                perimeter.append((ii, jj))
    
        add(index, perimeter)

price = sum(map(lambda key: plots[key][0] * len(plots[key][1]), plots.keys()))
print("Part 1 price:", price)

visited = []

def check_edge(edge: tuple, edges: list, direction = -1):
    i = edge[0]
    j = edge[1]
    if direction == -1:
        directions = [(i-1, j), (i, j+1), (i+1, j), (i, j-1)]
    else: directions = [(i+(-1*abs(direction-2)+1), j+(-1*abs(direction-1)+1))]
    for d in range(len(directions)):
        ii = directions[d][0]
        jj = directions[d][1]
        if ((ii, jj) in edges) and ((ii, jj) not in visited):
            visited.append(edge)
            edges.remove(edge)
            if direction == -1: direction = d
            return check_edge((ii, jj), edges, direction)
    edges.remove(edge)
    return 1

discount_price = 0
for key in plots.keys():
    edges = plots[key][1].copy()
    sides = 0
    while len(edges) > 0:
        edge = edges[0]
        visited = []
        sides += check_edge(edge, edges)
    discount_price += plots[key][0] * sides
    #print(f"key:{key}, sides:{sides}, area:{plots[key][0]}")

print("Part 2 price:", discount_price)

 #       grd[0] + (-1*abs(dir-2)+1),
 # 27   │         grd[1] + (-1*abs(dir-1)+1)