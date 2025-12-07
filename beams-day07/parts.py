import sys

filename = "sample.txt"
if len(sys.argv) >= 2:
    filename = sys.argv[1]

lines = list(map(str.strip,open(filename).readlines()))

first_beam = lines[0].index("S")
beams = [0] * len(lines[0])
beams[first_beam] = 1

splits = 0

print(lines[0].replace(".", " "))
for line in lines[1:]:
    for beam_i, amt in enumerate(beams.copy()):
        if amt == 0: continue
        if line[beam_i] == "^":
            beams[beam_i-1] += amt
            beams[beam_i+1] += amt
            beams[beam_i] = 0
            splits += 1
    for index, ch in enumerate(line):
        if beams[index]:
            print("|", end="")
        else:
            if ch == ".": ch = " "
            print(ch, end="")
    print()

print("Part 1 splits:")
print(splits)

print("Part 2 timelines:")
print(sum(beams))
