lines = open("input.txt").readlines()

def is_dots(line:str):
    for c in line:
        if c != ".":
            return False
    return True


def transpose(lines:list):
    res = ['' for i in range(len(lines[0]))]
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            res[j] += lines[i][j]
    return res


def get_galaxies(space:list):
    galaxies = []
    for i in range(len(space)):
        for j in range(len(space[i])):
            c = space[i][j]
            if c == "#":
                galaxies.append((i,j))
    return galaxies


def get_distance_sum(expansion:int):
    space = []
    for line in lines:
        space.append(line.strip())
    galaxies = get_galaxies(space)
    
    empty_rows = []
    empty_cols = []
    for i in range(len(space)):
        if is_dots(space[i]):
            empty_rows.append(i)
    trans_space = transpose(space)
    for i in range(len(trans_space)):
        if is_dots(trans_space[i]):
            empty_cols.append(i)
    
    sum = 0
    for i in range(len(galaxies) - 1):
        for j in range(i+1, len(galaxies)):
            g1y = galaxies[i][0]
            g1x = galaxies[i][1]
            g2y = galaxies[j][0]
            g2x = galaxies[j][1]
            
            dist = 0
            for row in range(min(g1y, g2y)+1, max(g1y, g2y) + 1):
                if empty_rows.__contains__(row):
                    dist += expansion
                else:
                    dist += 1
            for col in range(min(g1x, g2x)+1, max((g1x, g2x)) + 1):
                if empty_cols.__contains__(col):
                    dist += expansion
                else:
                    dist += 1
            sum += dist
    
    return sum


def main():
    #   Part 1
    expansion = 2
    print(f'Part 1: Sum: {get_distance_sum(expansion)}')
    
    #   Part 2
    expansion = 10 ** 6
    print(f'Part 2: Sum: {get_distance_sum(expansion)}')


if __name__ == "__main__":
    main()
