lines = open("input.txt").readlines()

def transpose(grid:list):
    res = ['' for i in range(len(grid[0]))]
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            res[col] += grid[row][col]
    return res

def find_mirror(grid:list):
    mir_index = -1
    for i in range(1, len(grid)):
        if grid[i] == grid[i-1]:
            j = 0
            while True:
                if (i+j >= len(grid)) | (i-j-1 < 0):
                    mir_index = i
                    break
                if grid[i+j] != grid[i-j-1]:
                    break
                j += 1
        if mir_index > 0:
            break
    return mir_index
                    


def main():
    grids = [[]]
    grid_ind = 0
    for line in lines:
        line = line.strip()
        if line == '':
            grids.append([])
            continue
        grids[-1].append(line)
    
    print("-------------")
    #for g in grids:
    #    print(f'Grid!')
    #    for l in transpose(g):
    #        print(l)
            
    sum = 0
    mul = 100
    for grid in grids:
        vertical = False
        ind = find_mirror(grid)
        if ind < 0:
            ind = find_mirror(transpose(grid))
            sum += ind
            vertical = True
        else:
            sum += mul * ind
            
        for l in grid:
            print(l)
        print(f'Vertical: {vertical}, ind: {ind}')
        if ind < 0:
            break
    print(f'Part 1: Sum: {sum}')

            
            
if __name__ == "__main__":
    main()