lines = open("input.txt").readlines()


def main():
    #   Part 1
    product = 1
    
    races = [[] for k in range(4)]
    i = 0
    for s in lines[0].split(":")[1].strip().split(" "):
        if s != '':
            races[i].append(int(s))
            i += 1
    
    i = 0
    for s in lines[1].split(":")[1].strip().split(" "):
        if s != '':
            races[i].append(int(s))
            i += 1
    print(races)
    
    for race in races:
        time = race[0]
        dist = race[1]
        times = []
        for h in range(1, time + 1):
            times.append(h * (time - h))
        count = 0
        for t in times:
            if t > dist:
                count += 1
        product *= count
    

    print(f'Part 1: Product: {product}')
    
    #   Part 2
    time = ""
    dist = ""
    for race in races:
        time += str(race[0])
        dist += str(race[1])
    print(f'Time:     {time}')
    print(f'Distance: {dist}')
    time = int(time)
    dist = int(dist)
    
    times = []
    for h in range(1, time + 1):
        times.append(h * (time - h))
    count = 0
    for t in times:
        if t > dist:
            count += 1
    
    print(f'Part 2: count: {count}')



if __name__ == "__main__":
    main()