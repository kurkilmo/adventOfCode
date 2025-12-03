import sys

filename = "input.txt"
if len(sys.argv) >= 2:
    filename = sys.argv[1]

lines = open(filename).readlines()

banks = list(map(
    lambda line: list(map(int, line.strip())),
    lines
))

joltage_p1 = 0
joltage_p2 = 0

def find_joltage(bank: list, amount: int) -> int:
    joltage = 0
    max_index = 0

    for exp in range(amount-1, -1, -1):
        end_ind = -exp
        if end_ind == 0: end_ind = None

        max_num = max(bank[max_index:end_ind])
        max_index = bank[max_index:end_ind].index(max_num) + 1 + max_index

        joltage += max_num * 10**exp

    return joltage


for bank in banks:
    # Part 1: find largest number, then find largest number after that
    joltage_p1 += find_joltage(bank, 2)

    # Part 2: twelve largest numbers
    joltage_p2 += find_joltage(bank, 12)


print("Part 1 total joltage:")
print(joltage_p1)
print("Part 2 total joltage:")
print(joltage_p2)