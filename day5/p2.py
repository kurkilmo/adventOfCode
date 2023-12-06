#
#   Doesn't work yet
#
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
    
    # Get seeds and run maps
    min_location = None
    seed_ranges = lines[0].split(":")[1].split(" ")[1:]
    i = 0
    while (i < len(seed_ranges)):
        seeds = []
        seed_range = [int(seed_ranges[i]), int(seed_ranges[i+1])]
        #seed_range.sort()
        print(f'Startseed: {seed_range[0]}, Length: {seed_range[1]}')
        for j in range(seed_range[1]):
            seeds.append(seed_range[0] + j)
        print("seeds calculated")
    
        for seed in seeds:
            for map in maps:
                seed = whole_map(seed, map)
            if min_location == None:
                min_location = seed
            elif seed < min_location:
                min_location = seed
        
        i += 2
    
    print(f'min: {min_location}')

if __name__ == "__main__":
    main()