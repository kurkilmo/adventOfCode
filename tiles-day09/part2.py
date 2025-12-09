import sys
import itertools
from tkinter import Tk, Canvas

def area(a, b):
    offs_x = 0
    if b[0] >= a[0]:
        offs_x = 1
    else:
        offs_x = -1
    offs_y = 0
    if b[1] >= a[1]:
        offs_y = 1
    else:
        offs_y = -1
    return abs(a[0]-(b[0]+offs_x)) * abs(a[1]+-(b[1]+offs_y))

filename = "sample.txt"
if len(sys.argv) >= 2:
    filename = sys.argv[1]

tiles: list[tuple[int]] = [] # List of coordinate tuples (x,y,z)
for line in open(filename, "r").readlines():
    tiles.append(tuple(map(int,line.strip().split(","))))

min_x = min(map(lambda a: a[0], tiles))
min_y = min(map(lambda a: a[1], tiles))
max_x = max(map(lambda a: a[0], tiles))
max_y = max(map(lambda a: a[1], tiles))
max_c = max(max_x, max_y)+1

# List of 2-combinations of tile pairs
combs = list(itertools.combinations(range(len(tiles)), 2))

for i in range(len(combs)):
    a, b = combs[i]
    jA = tiles[a]
    jB = tiles[b]
    # Add area info to combinations
    combs[i] = (a, b, area(jA, jB))

# Sort by area
combs.sort(key=lambda v: -v[2])

all_tiles = dict()
def check_key(key):
    try:
        return all_tiles[key]
    except KeyError:
        return None
#for i in range(max_c):
#    all_tiles.append([' '] * max_c)
#print(all_tiles)
for i in range(-1,len(tiles)-1):
    t1 = tiles[i]
    t2 = tiles[i+1]

    all_tiles[(t1[1], t1[0])] = 'X'
    #continue
    
    if t1[0] == t2[0]: # Same x = vertical line
        start = min(t1[1], t2[1])
        end = max(t1[1], t2[1])
        for y in range(start+1, end):
            all_tiles[(y, t1[0])] = '|'
    elif t1[1] == t2[1]: # Same y = horizontal line
        start = min(t1[0], t2[0])
        end = max(t1[0], t2[0])
        for x in range(start+1, end):
            all_tiles[(t1[1], x)] = '-'
    else:
        print("paska")

if max_c < 1000:
    for x in range(max_c):
        for y in range(max_c):
            try:
                print(all_tiles[(x,y)], end="")
            except KeyError:
                print(" ", end="")
        print()

window = Tk()
window.attributes('-type', 'dialog')
window_size = 1000

canvas = Canvas(
    master=window,
    width=window_size,
    height=window_size,
    bg="black"
)

def fit(v):
    res_min = 10
    res_max = window_size-10
    x, y = v
    x = res_min + ((x - min_x) / (max_x - min_x)) * (res_max - res_min)
    y = res_min + ((y - min_y) / (max_y - min_y)) * (res_max - res_min)
    return (x, y)

colors = {
    ' ': "white",
    'X': "red",
    "-": "green",
    "|": "blue"
}
for i in range(-1, len(tiles)-1):
    t1 = tiles[i]
    t2 = tiles[i+1]
    x1, y1 = fit(t1)
    x2, y2 = fit(t2)

    x = (t1[0]+t2[0]) // 2
    y = (t1[1]+t2[1]) // 2

    try:
        color = colors[all_tiles[(y, x)]]
    except IndexError:
        color = "yellow"

    canvas.create_line(x1, y1, x2, y2, fill=color, width=2)

box_ind = 0 # 38761
def draw_dot(x, y):
    canvas.delete("dot")
    canvas.create_line(x,y,x+1,y+1, fill="white", width=1, tags="dot")
    #canvas.after(10, lambda: draw_dot(x+1,y+1, mx, my))
collided = False
def draw_box(event = None):
    global collided
    global box_ind
    canvas.delete("box")
    canvas.delete("dot")
    comb = combs[box_ind]

    t1 = tiles[comb[0]]
    t2 = tiles[comb[1]]

    #print(f"{t1=}, {t2=}")

    x1, y1 = fit(t1)
    x2, y2 = fit(t2)

    canvas.create_rectangle(x1,y1,x2,y2, outline="red", width=1, tags="box")
    end_rad = 6
    canvas.create_oval(x1-end_rad,y1-end_rad,x1+end_rad,y1+end_rad, outline="yellow", tags="dot")
    canvas.create_oval(x2-end_rad,y2-end_rad,x2+end_rad,y2+end_rad, outline="yellow", tags="dot")

    min_x = min(t1[0], t2[0])
    max_x = max(t1[0], t2[0])
    min_y = min(t1[1], t2[1])
    max_y = max(t1[1], t2[1])

    collided = False
    def check(x, y, c):
        global collided
        try:
            d = all_tiles[(y,x)]
            if d == c:
                if c == "-" and y in (min_y, max_y): return
                if c == "|" and x in (min_x, max_x): return
                #print(f"{x=},{y=}")
                xx, yy = fit((x, y))
                #canvas.create_line(xx,yy,xx+10,yy+10, fill="white", width=10, tags="dot")
                canvas.create_oval(xx-2,yy-2,xx+2,yy+2, outline="white", tags="dot")
                collided = True
                #return
            if d == "X":
                xx, yy = fit((x, y))
                outline = "green"
                if c == "-":
                    if y == min_y:
                        if check_key((y-1,x)) and check_key((x+1,y)):
                            outline="red"
                    #elif y == max_y and x == max_x-1:
                    #    if check_key(())
                    elif x == max_x:
                        if check_key((y,x-1)): outline="red"
                        pass # menossa alaspäin oikeassa päässä
                    elif x == min_x:
                        if check_key((y,x+1)): outline="red"
                        pass # alaspäin vasemmalla
                elif c == "|":
                    if x == min_x:
                        pass
                    elif y == max_y:
                        if check_key((y-1,x)): outline="red"
                        pass # oikealle alhaalla
                    elif y == min_y:
                        if check_key((y+1,x)): outline="red"
                        pass # oikealle ylhäällä
                if outline == "red":
                    #print(f"illegal corner {x} {y}")
                    collided = True
                canvas.create_oval(xx-3,yy-3,xx+3,yy+3, outline=outline, tags="dot")
        except KeyError: pass

    for x in range(min_x, max_x):
        for y in (min_y, max_y):
            check(x,y, "|")
        #    if collided: break
        #if collided: break

    for y in range(min_y, max_y):
        for x in (min_x, max_x):
            check(x,y, "-")
        #    if collided: break
        #if collided: break
    
    #if collided:
    #    canvas.after(1, draw_box)
    #else:
    s = "good"
    if collided: s = "BAD"
    print(f"index {box_ind}, {s}")
    #print(area(t1, t2))

    box_ind += 1

def go_back(event):
    global box_ind
    box_ind -= 2
    draw_box()

canvas.bind("<Button-1>", draw_box)
canvas.bind("<Button-3>", go_back)
canvas.after(1, draw_box)

canvas.pack()
window.mainloop()