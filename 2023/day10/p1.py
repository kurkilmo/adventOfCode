lines = open("input.txt").readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()
    for j in range(len(lines)):
        if lines[i][j] == "S":
            start = [i,j]

def main():
    print(start)
    prev_coord = start.copy()
    coord = [start[0], start[1]+1]
    
    count = 1
    
    while coord != start:
        char = lines[coord[0]][coord[1]]
        cur_coord = coord.copy()
        same_line = prev_coord[0] == coord[0]
        match char:
            case '|':
                if prev_coord[0] < coord[0]:
                    coord[0] += 1
                else:
                    coord[0] -= 1
            case '-':
                if prev_coord[1] < coord[1]:
                    coord[1] += 1
                else:
                    coord[1] -= 1
            case 'L':
                if same_line:
                    coord[0] -= 1
                else:
                    coord[1] += 1
            case 'J':
                if same_line:
                    coord[0] -= 1
                else:
                    coord[1] -= 1
            case '7':
                if same_line:
                    coord[0] += 1
                else:
                    coord[1] -= 1
            case 'F':
                if same_line:
                    coord[0] += 1
                else:
                    coord[1] += 1
            case '.':
                print(f"saatana. {prev_coord} -> {coord}")
                return
        prev_coord = cur_coord
        count += 1
    print(f'Count: {count}, count/2: {count / 2}')
        
            

if __name__ == "__main__":
    main()