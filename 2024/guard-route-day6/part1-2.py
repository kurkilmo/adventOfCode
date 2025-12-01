import time, sys
from visualize import visualize, insert_string

lines = open("input.txt").readlines()
size = len(lines)

visual = len(sys.argv) >= 2
delay = 0
try:
    delay = float(sys.argv[1])
except: pass

guard = []
guard_dir = 0

for i in range(size):
    for j in range(size):
        if lines[i][j] in "^>v<":
            guard = [i, j]
            guard_dir = "^>v<".index(lines[i][j])
            break

def next_square(dir, grd = None):
    if not grd: grd = guard
    return [
        grd[0] + (-1*abs(dir-2)+1),
        grd[1] + (-1*abs(dir-1)+1)
    ]

def is_out_of_bounds(lst: list):
    return lst[0] < 0 or lst[0] >= size or lst[1] < 0 or lst[1] >= size

visited = [(['.'] * size) for _ in range(size)]

def update_visited(lst: list, grd, dir):
    i = grd[0]
    j = grd[1]
    if lst[i][j] == '.':
        lst[i][j] = "↑→↓←"[dir]

def is_obstacle(lst:list):
    try:
        return lines[lst[0]][lst[1]] == "#"
    except:
        return False

def check_new_obstacle():
    dir = (guard_dir + 1) % 4
    new_guard = [guard[0], guard[1]]
    visited_check = [(['.'] * size) for _ in range(size)]
    loop = False
    while True:
        i = new_guard[0]
        j = new_guard[1]
        if is_out_of_bounds(new_guard): break
        if is_obstacle(next_square(dir, new_guard)) or next_square(dir, new_guard) == next_square(guard_dir):
            dir = (dir + 1) % 4
        if visited_check[i][j] == "↑→↓←"[dir]:
            loop = True
            break
        update_visited(visited_check, new_guard, dir)

        while is_obstacle(next_square(dir, new_guard)) or next_square(dir, new_guard) == next_square(guard_dir):
            dir = (dir + 1) % 4

        new_guard = next_square(dir, new_guard)
    #if visual and loop: 
    #    insert_string(visualize(lines, size, obstacles_check, new_guard, dir, new_obstacles,visited_check))
    #    input()
    #    time.sleep(delay)
    return loop

new_obstacles = []
if visual: print(visualize(lines, size, guard, guard_dir, new_obstacles,visited))
while True:
    if check_new_obstacle():
        new_obstacles.append(next_square(guard_dir))

    if visual: insert_string(visualize(lines, size, guard, guard_dir, new_obstacles,visited))

    if is_obstacle(next_square(guard_dir)):
        guard_dir = (guard_dir + 1) % 4
    
    while is_obstacle(next_square(guard_dir)):
        guard_dir = (guard_dir + 1) % 4
    guard = next_square(guard_dir)

    if (guard[0] >= size or guard[0] < 0 or guard[1] >= size or guard[1] < 0):
        break

    update_visited(visited, guard, guard_dir)
    if visual: time.sleep(delay)

print(visualize(lines, size, guard, guard_dir, new_obstacles,visited))

visited_count = 1
for a in visited:
    for b in a:
        visited_count += b != "."
print("Part 1:", visited_count)
print("Part 2:", visualize(lines, size, guard, guard_dir, new_obstacles,visited).count("O"))
