from PIL import Image
import numpy as np

#
#   I found the area in the loop using the saved image file and the console output in photoshop
#

lines = open("input.txt").readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()
    for j in range(len(lines)):
        if lines[i][j] == "S":
            start = [i,j]
drawing = []
for i in range(len(lines)):
    drawing.append([])
    for j in range(len(lines[i])):
        if [i,j] == start:
            drawing[i].append('╚')
        else:
            drawing[i].append(" ")
            
def save_image(s:list):
    x_size = len(s[0])
    y_size = len(s)
    print(x_size)
    print(y_size)
    a = np.zeros((x_size, y_size))
    for i in range(x_size):
        for j in range(y_size):
            if s[i][j] == " ":
                a[i][j] = 0
            else:
                a[i][j] = 1
    
    img = Image.fromarray(a)
    
    img.save("p2.tiff")
    #for i in range(y_size):
    #    for j in range(x_size):
    #        img.
    
    
def main():
    print(start)
    prev_coord = start.copy()
    coord = [start[0], start[1]+1]
    
    while coord != start:
        char = lines[coord[0]][coord[1]]
        cur_coord = coord.copy()
        same_line = prev_coord[0] == coord[0]
        c = ' '
        match char:
            case '|':
                c = '│'
                if prev_coord[0] < coord[0]:
                    coord[0] += 1
                else:
                    coord[0] -= 1
            case '-':
                c = '─'
                if prev_coord[1] < coord[1]:
                    coord[1] += 1
                else:
                    coord[1] -= 1
            case 'L':
                c = '└'
                if same_line:
                    coord[0] -= 1
                else:
                    coord[1] += 1
            case 'J':
                c = '┘'
                if same_line:
                    coord[0] -= 1
                else:
                    coord[1] -= 1
            case '7':
                c = '┐'
                if same_line:
                    coord[0] += 1
                else:
                    coord[1] -= 1
            case 'F':
                c = '┌'
                if same_line:
                    coord[0] += 1
                else:
                    coord[1] += 1
            case '.':
                print(f"saatana. {prev_coord} -> {coord}")
                return
        drawing[cur_coord[0]][cur_coord[1]] = c
        prev_coord = cur_coord
    
    for i in range(len(lines)):
        s = ''
        for j in range(len(lines[i])):
            c = drawing[i][j]
            if c != " ":
                c = "█"
            s += c
        
        print(s)
    for i in range(len(lines)):
        s = ''
        for j in range(len(lines[i])):
            c = drawing[i][j]
            s += c
    
        print(s)
        
    save_image(drawing)
            

if __name__ == "__main__":
    main()