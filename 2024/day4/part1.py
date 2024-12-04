lines = open("input.txt").readlines()
prnt = print
print = lambda s: None

def transpose(lines:list):
    res = ['' for i in range(len(lines[0]))]
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            res[j] += lines[i][j]
    return res[:-1]

def is_xmas(lst:list, ind: int):
    return lst[ind:ind+4] == "XMAS"

xmases = 0

def sum_xmas_simple(rows:list):
    sum = 0
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            # Normal
            sum += is_xmas(rows[i], j)

            # Reverse
            sum += is_xmas(rows[i][::-1], j)
    return sum


xmases += sum_xmas_simple(lines)

# Transposed
trans = transpose(lines)
xmases += sum_xmas_simple(trans)

# Diagonal
def mirror(lst: list):
    res = lst.copy()
    for i in range(len(lst)):
        res[i] = res[i].strip()[::-1]
    return res

def diagonalize(lst: list):
    ln = len(lst)
    diag = ['' for _ in range(ln*2)]
    for i in range(ln):
        for j in range(i+1):
            diag[i] += lst[i-j][j]

    append_index = 0
    for i in reversed(range(ln)):
        ii = ln+1-i
        for j in range(i):
            di = ln-1-j
            dj = ii+j-1
            diag[ln + append_index] += lst[di][dj]
        append_index += 1
    return diag

xmases += sum_xmas_simple(diagonalize(lines))
xmases += sum_xmas_simple(diagonalize(mirror(lines)))

prnt("Part 1:", xmases)