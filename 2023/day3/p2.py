import re

lines = open("input2.txt").readlines()
print(f'len: {len(lines)}, w: {len(lines[0])}')

def is_number(text:str):
    return re.search("[0-9]",text) != None

def parsenumber(row:int, col:int):
    c = col
    res = ""
    while (is_number(lines[row][c])):
        res = lines[row][c] + res
        c -= 1
    c = col + 1
    after = 0
    while (is_number(lines[row][c])):
        res += lines[row][c]
        after += 1
        c += 1
        
    return (int(res), after != 0) # true, if row should be skipped

def main():
    sum = 0
    
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if lines[row][col] != "*":
                continue
            gears = []
            print(f'\nStar at {row}, {col}')
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (j == 0) & (i == 0):
                        continue
                    if is_number(lines[row+i][col+j]):
                        num, skip = parsenumber(row+i, col+j)
                        print(f'num: {num}, skip: {skip}')
                        gears.append(num)
                        if (i != 0) & skip:
                            break
            if len(gears) == 2:
                sum += (gears[0] * gears[1])
                print(f'gear 1: {gears[0]}, gear 2 {gears[1]}, ratio: {gears[0]*gears[1]}')
    
    print(f'Sum: {sum}')
    
if __name__ == "__main__":
    main()
            

