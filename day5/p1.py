lines = open("input.txt").readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()
    
def single_map(seed:int, dest_start:int, source_start:int, length:int):
    dest_start = int(dest_start)
    source_start = int(source_start)
    length = int(length)
    if (seed >= source_start) & (seed < (source_start + length)):
        return (dest_start + (seed - source_start), True)
    return (seed, False)

def whole_map(seed:int, map:list):
    res_seed = seed
    for m in map:
        res_seed, stop = single_map(seed, m[0], m[1], m[2])
        if stop:
            break
    return res_seed
    

def main():
    # Get seeds
    seeds = lines[0].split(":")[1].split(" ")[1:]
    for i in range(len(seeds)):
        seeds[i] = int(seeds[i])
    
    # Get maps
    maps = [[] for k in range(7)]
    line_index = 1
    map_index = 0
    while line_index < len(lines):
        #print(lines[line_index])
        line_index += 2
        while (lines[line_index] != ""):
            maps[map_index].append(lines[line_index].split(" "))
            line_index += 1
            if (line_index >= len(lines)):
                break
        map_index += 1
    
    #for i in range(len(maps)):
    #    print("Map:")
    #    for j in range(len(maps[i])):
    #        print(maps[i][j])
            
    locations = []
    for seed in seeds:
        for map in maps:
            seed = whole_map(seed, map)
        locations.append(seed)
    print(locations)
    print(f'min: {min(locations)}')

if __name__ == "__main__":
    main()