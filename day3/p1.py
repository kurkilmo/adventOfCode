import re

lines = open("input2.txt").readlines()
print(f'len: {len(lines)}, w: {len(lines[0])}')
rx = "[^a-zA-Z0-9.\n]"
numrx = "[0-9]"
def reg(pattern:str, text:str):
    return re.search(pattern,text) != None

def get_number(row:int, col:int):
    d1 = lines[row][col]
    res = str(d1)
    d2 = lines[row][col+1]
    d3 = lines[row][col+2]
    if reg(numrx,d2):
        res += str(d2)
        if reg(numrx, d3):
            res += str(d3)
    return res
    
def search(row:int, col:int, length:int):
    found = False
    for r in range(-1, 2):
        for c in range(-1, length+1):
            try:
                if reg(rx, lines[row+r][col+c]):
                    found = True
                    #print("found")
            except:
                pass#print(f'Exception: row:{row+r}, col:{col+c}')
    return found

def main():
    sum = 0

    for row in range(len(lines)):
        col = 0
        while col < len(lines[row]):
            ch = lines[row][col]
            if reg(numrx, ch):
                num = get_number(row,col)
                print(f'Number: {num}')
                if search(row,col,len(num)):
                    sum += int(num)
                    print("Adjacent character found")
                col += len(num) - 1
            col += 1
    
    print(f'Sum: {sum}')


if __name__ == "__main__":
    main()