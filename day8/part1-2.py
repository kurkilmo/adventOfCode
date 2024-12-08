import itertools
lines = open("input.txt").readlines()

antennas = dict()

size = len(lines)

for i in range(len(lines)):
    for j in range(len(lines[i])):
        char = lines[i][j]
        if char == '.' or char == '\n': continue
        if char in antennas.keys():
            antennas[char].append((i, j))
        else:
            antennas[char] = [(i,j)]

antinodes = set()

def print_antinodes(nodes):
    res_map = ""
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] != '.' or (i,j) not in nodes:
                res_map += lines[i][j]
            else:
                res_map += "#"
    print(res_map)

def is_in_bounds(node: tuple):
    return (node[0] in range(size)) and (node[1] in range(size))


# Part 1
for key in antennas.keys():
    for combination in itertools.combinations(antennas[key], 2):
        ant_a = combination[0]
        ant_b = combination[1]

        d_i = ant_b[0] - ant_a[0]
        d_j = ant_b[1] - ant_a[1]
    
        node_a = (ant_b[0] + d_i, ant_b[1] + d_j)
        node_b = (ant_a[0] - d_i, ant_a[1] - d_j)

        for node in [node_a, node_b]:
            if is_in_bounds(node):
                antinodes.add(node)

print_antinodes(antinodes)
print("Part 1:", len(antinodes))

# Part 2
antinodes.clear()
for key in antennas.keys():
    # Antennas as antinodes
    for antenna in antennas[key]:
        if len(antennas[key]) >= 2:
            antinodes.add(antenna)
    
    # Other antinodes
    for combination in itertools.combinations(antennas[key], 2):
        ant_a = combination[0]
        ant_b = combination[1]

        d_i = ant_b[0] - ant_a[0]
        d_j = ant_b[1] - ant_a[1]

        node_a = (ant_b[0] + d_i, ant_b[1] + d_j)
        node_b = (ant_a[0] - d_i, ant_a[1] - d_j)
        
        while is_in_bounds(node_a):
            antinodes.add(node_a)
            node_a = (node_a[0] + d_i, node_a[1] + d_j)

        while is_in_bounds(node_b):
            antinodes.add(node_b)
            node_b = (node_b[0] - d_i, node_b[1] - d_j)

print_antinodes(antinodes)
print("Part 1:", len(antinodes))