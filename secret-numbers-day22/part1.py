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

def add(key, value):
    try:
        sequences[key].append(value)
    except KeyError:
        sequences[key] = [value]

def price(secret:int):
    return int(str(secret)[-1])

for num in initial_nums:
    sequence = []
    
    prev = num
    for i in range(1,5):
        secret = next_secret(prev)
        diff = price(secret) - price(prev)
        sequence.append(diff)
        prev = secret

    add(tuple(sequence), price(secret))

    for i in range(1, rounds):
        secret = next_secret(prev)
        diff = price(secret) - price(prev)
        sequence.pop(0)
        sequence.append(diff)
        prev = secret

        add(tuple(sequence), price(secret))

max_price = max(list(map(sum, sequences.values())))
print(sequences[(-2,1,-1,3)])
for seq in sequences.keys():
    s = sum(sequences[seq])
    if s >= 23:
        print(f"{seq}:{s}")
print(f"Part 2: max bananas: {max_price}")