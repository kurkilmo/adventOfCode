lines = open("input.txt").readlines()

def main():
    sum = 0
    
    for line in lines:
        line = line[4:-1].strip()
        print(line)
        right_numbers = []
        for num in line.split("|")[0].split(":")[1].split(" "):
            num = num.strip()
            if num == '':
                continue
            right_numbers.append(int(num.strip()))
        got_numbers = []
        for num in line.split("|")[1].split(" "):
            num = num.strip()
            if num == '':
                continue
            got_numbers.append(int(num))
        #print(right_numbers)
        #print(got_numbers)
        
        rights = 0
        for rn in right_numbers:
            if got_numbers.__contains__(rn):
                rights += 1
        points = 2 ** (rights - 1)
        points = float.__floor__(points * 1.0)
        print(points)
        sum += points
    
    print(f'Sum: {sum}')

if __name__ == "__main__":
    main()