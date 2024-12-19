lines = open("input.txt").readlines()

def is_x_mas(i: int, j:int):
    if (i < 0 or i >= len(lines)-1 or j < 0 or j >= len(lines)-1): return False

    # Hyi saatana :D
    if (lines[i-1][j-1] == 'M') and (lines[i+1][j+1] == 'S'):
        if (lines[i+1][j-1] == 'M') and (lines[i-1][j+1] == 'S'):
            return True
        if (lines[i+1][j-1] == 'S') and (lines[i-1][j+1] == 'M'):
            return True
    if (lines[i-1][j-1] == 'S') and (lines[i+1][j+1] == 'M'):
        if (lines[i+1][j-1] == 'M') and (lines[i-1][j+1] == 'S'):
            return True
        if (lines[i+1][j-1] == 'S') and (lines[i-1][j+1] == 'M'):
            return True
    
    return False

count = 0
for i in range(len(lines)):
    for j in range(len(lines)):
        if lines[i][j] == 'A':
            count += is_x_mas(i, j)

print("Part 2:", count)