lines = open("testinput.txt").readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()
    
def transpose(lines:list):
    res = ['' for i in range(len(lines[0]))]
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            res[col] += lines[row][col]
    return res

def mirror_hor(lines:list):
    res = []
    for l in lines:
        res.append(l[::-1])
    return res

def mirror_ver(lines:list):
    return lines[::-1]

def tostring(line:list):
    res = ''
    for c in line:
        res += c
    return res

def pack_left(lines:list):
    result = []
    
    for row in range(len(lines)):
        line = []
        for col in range(len(lines[row])):
            ch = lines[row][col]
            match ch:
                case '.' | '#':
                    line.append(ch)
                case 'O':
                    line.append('.')
                    i = col - 1
                    while True:
                        if (line[i] != '.') | (i == -1):
                            line[i+1] = 'O'
                            break
                        i -= 1
        result.append(tostring(line))
    return result

def get_load(lines:list):
    sum = 0
    for i in range(len(lines)):
        amount = len(lines) - i
        sum += amount * lines[i].count('O')
    return sum

def main():
    #   Part 1
    tr_lines = transpose(lines)
    result = pack_left(tr_lines)
    tr_result = transpose(result)
    sum = get_load(tr_result)
    print(f'Part 1: sum: {sum}')
    
    #   Part 2  (Doesnt work)
    cycle_count = 10
    res = lines.copy()
    for r in res:
        print(r)
    for c in range(cycle_count):
        res = transpose(pack_left(transpose(res)))
        res = pack_left(res)
        res = mirror_ver(transpose(pack_left(transpose(mirror_ver(res)))))
        res = mirror_hor(pack_left(mirror_hor(res)))
        print('\n-----\n')
        for r in res:
            print(r)
    print(f'Part 2: sum: {get_load(res)}, cycle count: {cycle_count}')
    
            

if __name__ == "__main__":
    main()