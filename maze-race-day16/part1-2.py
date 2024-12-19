import sys
import time

if len(sys.argv) >= 2:
    filename = sys.argv[1]
else:
    filename = "2sample.txt"

sys.setrecursionlimit(5000)

data = open(filename).readlines()
size = len(data)

walls = []
start = ()
end = ()
route = dict()

for i in range(size):
    for j in range(size):
        coord = (i, j)
        match data[i][j]:
            case '#':
                walls.append(coord)
            case 'S':
                start = coord
            case 'E':
                end = coord

def insert_string(s: str):
    lines = s.split('\n')
    #lines.reverse()
    sys.stdout.write('\33[A' * (len(lines)))
    for line in lines:
        sys.stdout.write(line + '\n')
    sys.stdout.flush()

def visual(pos = (0,0), cur_route = None):
    if cur_route:
        keys = cur_route
    else:
        keys = route.keys()
    res = ""
    for i in range(size):
        line = ""
        for j in range(size):
            c = (i,j)
            if c == pos: line += "O"
            elif data[c[0]][c[1]] == '#': line += "#"
            elif c == start: line += "S"
            elif c == end: line += "E"
            elif c in keys: line += "↑→↓←"[route[c][0]]
            else: line += " "
        res += line + "\n"
    res += str(pos)
    return res

end_scores = []

def next_square(direction, square):
    return (
        square[0] + (-1*abs(direction-2)+1),
        square[1] + (-1*abs(direction-1)+1)
    )

def dir_left(direction):
    return (direction - 1) % 4

def dir_right(direction):
    return (direction + 1) % 4

def traverse(score, pos, direction, current_route):
    #insert_string(visual(pos, current_route))
    #time.sleep(0.1)

    if pos in route.keys():
        if route[pos][1] < (score): return

    left  = next_square(dir_left(direction) , pos)
    right = next_square(dir_right(direction), pos)

    route[pos] = (direction, score)
    if pos == end:
        end_scores.append((score, current_route + [pos]))
        return
    
    nxt = next_square(direction, pos)
    if data[nxt[0]][nxt[1]] != '#':
        traverse(score+1, nxt, direction, current_route + [pos])
        route[pos] = (direction, score+1)
    if data[right[0]][right[1]] != '#':
        traverse(score+1001, right, dir_right(direction), current_route + [pos])
        route[pos] = (direction, score+1001)
    if data[left[0]][left[1]] != '#':
        traverse(score+1001, left, dir_left(direction), current_route + [pos])
        route[pos] = (direction, score+1001)


#sys.stdout.write(visual())
sys.stdout.flush()
try:
    traverse(0, start, 1, [start])
except KeyboardInterrupt:
    pass

min_score = min(map(lambda a: a[0], end_scores))
print(f"Minimum score: {min_score}")

min_paths = set()
for score in filter(lambda a: a[0] == min_score, end_scores):
    for spot in score[1]:
        min_paths.add(spot)

#for i in range(size):
#    line = ""
#    for j in range(size):
#        if data[i][j] == "#": line += "#"
#        elif (i,j) in min_paths: line += "o"
#        else: line += '.'
#    print(line)

print(f"Spots along best paths: {len(min_paths)}")