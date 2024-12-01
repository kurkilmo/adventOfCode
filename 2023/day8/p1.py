import math

lines = open("input.txt").readlines()
lines[0] = lines[0].strip()


def check_keys(keys:list):
    for key in keys:
        if k[2] != "Z":
            return False
    return True

def main():
    #   Format input
    dirs = []
    for i in range(len(lines[0])):
        c = lines[0][i]
        if c == "L":
            dirs.append(0)
        elif c == "R":
            dirs.append(1)

    map = dict()

    for i in range(2,len(lines)):
        spl = lines[i].split(" = ")
        address = spl[0]
        dests = spl[1].split(", ")
        left = dests[0][1:]
        right = dests[1][0:-2]
        map[address] = (left, right)
    
    #   Part 1
    key = "AAA"
    count = 0
    while (key != "ZZZ"):
        direction = dirs[count % len(dirs)]
        key = map[key][direction]
        count += 1
    print(f'Part 1: Count: {count}')
    
    #   Part 2 (Doesnt work)
    keys = []
    for key in map.keys():
        if key[2] == "A":
            keys.append(key)
    
    print(keys)
    loop_lengths = []
    for i in range(len(keys)):
        first = map[keys[i]][dirs[0]]
        count = 1
        key = map[first][dirs[count % len(dirs)]]
        while (key != first):
            count += 1
            key = map[key][dirs[count % len(dirs)]]
        loop_lengths.append(count)
        
    print(loop_lengths)
    
    lcm = loop_lengths[0]
    for i in range(1, len(loop_lengths)):
        lcm = math.lcm(lcm, loop_lengths[i])
    
    print(f'Part 2: Steps: {lcm}')
        

if __name__ == "__main__":
    main()
    interval = 100000
    #while not check_keys(keys):
    #    for key_ind in range(0,len(keys)):
    #        keys[key_ind] = map[keys[key_ind]][dirs[count % len(dirs)]]
    #    count += 1
    #    #print(keys)
    #    if (count % interval == 0):
    #        print(f'Count: {count}, Keys: {keys}')