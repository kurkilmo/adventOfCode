lines = open("input.txt").readlines()

lines_counts = dict()
for i in range(len(lines)):
    lines_counts[i+1] = 1
matches_on_lines = dict()

def rec(line:int):
    wins = matches_on_lines[line]
    for i in range(1, wins + 1):
        lines_counts[line+i] += 1
        rec(line + i)
    

def main():
    sum = 0
    
    for i in range(len(lines)):
        line = lines[i][4:-1].strip()
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
        
        matches_on_lines[i+1] = rights
        
    for ticket in range(1, len(lines)+1):
        rec(ticket)

    for val in lines_counts.values():
        sum += val

    print(f'Sum: {sum}')

if __name__ == "__main__":
    main()