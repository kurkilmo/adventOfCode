import sys

if len(sys.argv) >= 2:
    filename = sys.argv[1]
else:
    filename = "sample0.txt"

data = open(filename).readlines()

reg_A = int(data[0].split(": ")[-1].strip())
reg_B = int(data[1].split(": ")[-1].strip())
reg_C = int(data[2].split(": ")[-1].strip())

def initialize_registers():
    global reg_B, reg_C
    reg_B = int(data[1].split(": ")[-1].strip())
    reg_C = int(data[2].split(": ")[-1].strip())


program = data[-1].split(": ")[-1].strip().split(',')
program = list(map(int, program))

print(f"Register A: {reg_A}")
print(f"Register B: {reg_B}")
print(f"Register C: {reg_C}")

print("Program:\n", program)


def combo(operand):
    if operand <= 3: return operand
    return [reg_A, reg_B, reg_C][operand-4]


def execute():
    global reg_A, reg_B, reg_C
    out = []
    pointer = 0
    while pointer < len(program):
        operand = program[pointer+1]
        div = lambda: reg_A // (2 ** combo(operand))
        match program[pointer]:
            case 0: # ADV
                reg_A = div()
            case 1: # BXL
                reg_B = reg_B ^ operand
            case 2: # BST
                reg_B = combo(operand) % 8
            case 3: # JNZ
                if reg_A != 0:
                    pointer = operand
                    continue
            case 4: # BXC
                reg_B = reg_B ^ reg_C
            case 5: # OUT
                value = combo(operand) % 8
                if program[len(out)] != value:
                    return out
                out.append(value)
            case 6: # BDV
                reg_B = div()
            case 7: # CDV
                reg_C = div()
        pointer += 2
    return out


# Part 1
#out = execute()
#print("\nPart 1 output:")
#print(','.join(list(map(str,out))))

# Part 2
out = []
A = 1007100000
while True:
    reg_A = A
    initialize_registers()
    if A % 10000 == 0:
        print(f"Executing with A={A}")
    out = execute()
    if out == program:
        break
    A += 1

print(f"Part 2: A={A}")
