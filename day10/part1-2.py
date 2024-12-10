import sys

try:
    filename = sys.argv[1] + ".txt"
except IndexError:
    filename = "input.txt"
data = open(filename).read().splitlines()

size = len(data)

grid = [[] for _ in range(size)]

for i in range(size):
    for j in range(size):
        grid[i].append(int(data[i][j]))

def equal(value, i ,j):
    if j < 0 or i < 0: return False
    try:
        return grid[i][j] == value
    except IndexError:
        return False

def check_route(i:int, j:int):
    if grid[i][j] == 9: return [(i,j)]
    val = grid[i][j]
    res = []
    if equal(val + 1, i-1, j):
        res += check_route(i-1, j)
    if equal(val + 1, i, j+1):
        res += check_route(i, j+1)
    if equal(val + 1, i+1, j):
        res += check_route(i+1, j)
    if equal(val + 1, i, j-1):
        res += check_route(i, j-1)
    return res

def check_distinct_routes(i:int, j:int):
    if grid[i][j] == 9: return 1
    val = grid[i][j]
    res = 0
    if equal(val + 1, i-1, j):
        res += check_distinct_routes(i-1, j)
    if equal(val + 1, i, j+1):
        res += check_distinct_routes(i, j+1)
    if equal(val + 1, i+1, j):
        res += check_distinct_routes(i+1, j)
    if equal(val + 1, i, j-1):
        res += check_distinct_routes(i, j-1)
    return res



sum_p1 = 0
sum_p2 = 0
for i in range(size):
    for j in range(size):
        if grid[i][j] == 0:
            nines = check_route(i,j)
            amount = len(set(nines))
            sum_p1 += amount

            distincts = check_distinct_routes(i, j)
            sum_p2 += distincts

print("Part 1:", sum_p1)
print("Part 2:", sum_p2)