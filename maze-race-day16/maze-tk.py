from tkinter import Tk, Canvas
import sys
import random

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

####################

def neighbors(point):
    (i, j) = point
    return list(filter(
        lambda c: c[0] in range(size) and c[1] in range(size),
        [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]
    ))

window = Tk()
window.attributes('-type', 'dialog')
window_size = 1000
block_size = window_size / size


canvas = Canvas(
    master=window,
    width=window_size,
    height=window_size,
    bg="black"
)

for wall in walls:
    wall_thickness = 2
    created = False
    for ne in neighbors(wall):
        if data[ne[0]][ne[1]] == "#":
            created = True
            canvas.create_line(
                wall[1]*block_size + (block_size / 2),
                wall[0]*block_size + (block_size / 2),
                ne[1]*block_size + (block_size / 2),
                ne[0]*block_size + (block_size / 2),
                fill="#919191",
                width=block_size / wall_thickness
            )
    if created:
        circle_size = (block_size / (wall_thickness * 2 + 0.5))
    else:
        circle_size = (block_size / (wall_thickness))
    if not created:
        canvas.create_oval(
            wall[1]*block_size + (block_size / 2) - circle_size,
            wall[0]*block_size + (block_size / 2) - circle_size,
            wall[1]*block_size + (block_size / 2) + circle_size,
            wall[0]*block_size + (block_size / 2) + circle_size,
            fill="#919191", outline="#919191"
        )

def color(i: int, target: int):
    bright = 0xff
    dark = 0x66
    res = dark + int((bright-dark) * (1 - (target-i) / target))
    return f"#{hex(res)[2:]}0000"

def draw_path(position, current_route, prev_pos):
    canvas.delete("stuff")
    canvas.create_oval(
        position[1]*block_size + (block_size/4) ,
        position[0]*block_size + (block_size/4) ,
        position[1]*block_size+block_size - (block_size/4) ,
        position[0]*block_size+block_size - (block_size/4) ,
        fill="red",
        tags="stuff"
    )
    l = len(current_route)
    for i in range(1, l):
        p1 = current_route[i-1]
        p2 = current_route[i]
        c = color(i, l)
        canvas.create_line(
            p1[1]*block_size + (block_size / 2),
            p1[0]*block_size + (block_size / 2),
            p2[1]*block_size + (block_size / 2),
            p2[0]*block_size + (block_size / 2),
            fill=c, tags="stuff", width=(block_size / 4)
        )

    # All visited
    #canvas.create_line(
    #        position[1]*block_size + (block_size / 2),
    #        position[0]*block_size + (block_size / 2),
    #        prev_pos[1]*block_size + (block_size / 2),
    #        prev_pos[0]*block_size + (block_size / 2),
    #        fill="#736f00", width=(block_size / 5)
    #)
    

#####################

def next_square(direction, square):
    return (
        square[0] + (-1*abs(direction-2)+1),
        square[1] + (-1*abs(direction-1)+1)
    )

def dir_left(direction):
    return (direction - 1) % 4

def dir_right(direction):
    return (direction + 1) % 4

end_scores = []

total_delay = 0
delay = 30

def traverse(score, pos, direction, current_route, prev_pos):
    global total_delay, delay
    total_delay += delay
    canvas.after(total_delay, lambda: draw_path(pos, current_route, prev_pos))

    if pos in route.keys():
        if route[pos][1] < (score): return

    left  = next_square(dir_left(direction) , pos)
    right = next_square(dir_right(direction), pos)

    route[pos] = (direction, score)
    if pos == end:
        end_scores.append((score, current_route + [pos]))
        return
    
    nxt = next_square(direction, pos)
    def go_straight():
        if data[nxt[0]][nxt[1]] != '#':
            traverse(score+1, nxt, direction, current_route + [pos], pos)
            route[pos] = (direction, score+1)
    def go_left():
        if data[left[0]][left[1]] != '#':
            traverse(score+1001, left, dir_left(direction), current_route + [pos], pos)
            route[pos] = (direction, score+1001)
    def go_right():
        if data[right[0]][right[1]] != '#':
            traverse(score+1001, right, dir_right(direction), current_route + [pos], pos)
            route[pos] = (direction, score+1001)
    dirs = [go_straight, go_left, go_right]
    random.shuffle(dirs)
    for d in dirs: d()

def begin():
    try:
        traverse(0, start, 1, [start], start)
    except KeyboardInterrupt:
        print("int")
        pass

canvas.after(1, begin)
#canvas.after(1, lambda: draw_path(start, []))
canvas.pack()

window.mainloop()