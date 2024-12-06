import time, sys
from visualize import visualize, insert_string

lines = open("input.txt").readlines()
size = len(lines)

visual = len(sys.argv) >= 2
delay = 0
try:
    delay = float(sys.argv[1])
except: pass

obstacles = []
guard = []
guard_dir = 0

for i in range(size):
    for j in range(size):
        if lines[i][j] == '#':
            obstacles.append([i,j])
        elif lines[i][j] in "^>v<":
            guard = [i, j]
            guard_dir = "^>v<".index(lines[i][j])

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
        lst[i][j] = "↑→↓←"[dir] #  	← 	↑ 	→ 	↓
    #elif lst[i][j] in "|-":
    #    lst[i][j] = "+"

def check_new_obstacle():
    dir = (guard_dir + 1) % 4
    obstacles_check = obstacles.copy()
    obstacles_check.append(next_square(guard_dir))
    new_guard = [guard[0], guard[1]]
    visited_check = [(['.'] * size) for _ in range(size)]
    while True:
        i = new_guard[0]
        j = new_guard[1]
        if is_out_of_bounds(new_guard): break
        if next_square(dir, new_guard) in obstacles_check:
            dir = (dir + 1) % 4
        if visited_check[i][j] == "↑→↓←"[dir] or visited_check[i][j] == "+":
            return True
        update_visited(visited_check, new_guard, dir)

        while next_square(dir, new_guard) in obstacles_check:
            dir = (dir + 1) % 4

        new_guard = next_square(dir, new_guard)
        #if visual: 
        #    insert_string(visualize(size, obstacles_check, new_guard, dir, new_obstacles,visited_check))
        #    time.sleep(delay)
    return False

new_obstacle_count = 0
new_obstacles = []
if visual: print(visualize(size, obstacles, guard, guard_dir, new_obstacles,visited))
while True:
    if check_new_obstacle():
        new_obstacle_count += 1
        new_obstacles.append(next_square(guard_dir))

    if visual: insert_string(visualize(size, obstacles, guard, guard_dir, new_obstacles,visited))

    if next_square(guard_dir) in obstacles:
        guard_dir = (guard_dir + 1) % 4
    
    while next_square(guard_dir) in obstacles:
        guard_dir = (guard_dir + 1) % 4
    guard = next_square(guard_dir)

    if (guard[0] >= size or guard[0] < 0 or guard[1] >= size or guard[1] < 0):
        break

    update_visited(visited, guard, guard_dir)
    if visual: time.sleep(delay)

visited_count = 0
for a in visited:
    for b in a:
        visited_count += b != "."
print("Part 1:", visited_count)
print("Part 2:", new_obstacle_count)
