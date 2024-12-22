import sys

if len(sys.argv) >= 2:
    filename = sys.argv[1]
else:
    filename = "sample.txt"

examples = {
    "029A": "<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A",
    "980A": "<v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A",
    "179A": "<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A",
    "456A": "<v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A",
    "379A": "<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A"
}

code = "029A"

codes = open(filename).read().split()

numpad = dict()
i = 0
for c in "789456123-0A":
    numpad[c] = (i // 3, i % 3)
    i += 1

i = 0
dirpad = dict()
for c in "-^A<v>":
    dirpad[c] = (i // 3, i % 3)
    i += 1

def move_sequence(keypad, sequence):
    pos = keypad["A"]
    result = ""
    for move in sequence:
        d_i = keypad[move][0] - pos[0]
        d_j = keypad[move][1] - pos[1]
        abs_i = abs(d_i)
        abs_j = abs(d_j)

        hor = "^v"[d_i > 0]
        ver = "<>"[d_j > 0]

        moves = hor * abs_i + ver * abs_j
        
        result += moves + "A"
        pos = keypad[move]

    return result

def complexity(sequence, code):
    return len(sequence) * int(code[:-1])

def example():
    code = "029A"
    s1 = move_sequence(numpad, code)
    print(s1)
    print("<A^A>^^AvvvA")
    s2 = move_sequence(dirpad, s1)
    print(s2)
    print("v<<A>>^A<A>AvA<^AA>A<vAAA>^A")
    s3 = move_sequence(dirpad, s2)
    print(s3)
    print("<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A")


complexity_sums = 0
for code in codes:
    s1 = move_sequence(numpad, code)
    s2 = move_sequence(dirpad, s1)
    s3 = move_sequence(dirpad, s2)

    print(s3)
    print(examples[code])
    print("\n")

    complexity_sums += complexity(s3, code)

print(f"Part 1 sum: {complexity_sums}")
