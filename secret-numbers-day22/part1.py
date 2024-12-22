import sys

if len(sys.argv) >= 2:
    filename = sys.argv[1]
else:
    filename = "sample.txt"

initial_nums = list(map(int, open(filename).readlines()))

prune = 16777216
def next_secret(num: int):
    mul = num * 64
    mix = mul ^ num
    pr = mix % prune

    div = pr // 32
    mix = div ^ pr
    pr = mix % prune

    mul = pr * 2048
    mix = mul ^ pr
    pr = mix % prune

    return pr


# Part 1
rounds = 2000

secrets_sum = 0
for num in initial_nums:
    ch = num
    for i in range(rounds):
        ch = next_secret(ch)
    #print(f"{num}: {ch}")
    secrets_sum += ch
print(f"Part 1: sum: {secrets_sum}")

# Part 2
sequences = dict()

for num in initial_nums:
    sequence = []
    prev = 0
    ch = num
    for i in range(rounds):
        #diff = 

        ch = next_secret(num)