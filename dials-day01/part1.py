import sys

filename = "input.txt"
if len(sys.argv) >= 2:
    filename = sys.argv[1]

lines = open(filename).read()

dial = 50 # Dial starts at 50
p_dial = 50
password_p1 = 0
password_p2 = 0

for line in lines.split('\n'):
    if len(line) == 0: continue

    direction = line[0]
    sign = 0

    if direction == "L": sign = -1
    elif direction == "R": sign = 1
    else: raise ValueError

    amount = int(line[1:])
    dial += sign * amount

    if dial % 100 == 0:
        password_p1 += 1

    password_p2 += abs(p_dial//100 - dial//100)

    if (direction == "L"):
        if (dial % 100 == 0):
            password_p2 += 1
        if (p_dial % 100 == 0):
            password_p2 -= 1


    p_dial = dial

print(f"Part 1 password:")
print(password_p1)

print(f"\nPart 2 password:")
print(password_p2)
