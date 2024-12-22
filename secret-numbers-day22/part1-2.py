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
    done_sequences = set()
    sequence = []
    
    prev = num
    i = 0
    while i < 4:
        secret = next_secret(prev)
        diff = price(secret) - price(prev)
        sequence.append(diff)
        prev = secret
        i += 1

    add(tuple(sequence), price(secret))

    while i < 2000:
        secret = next_secret(prev)
        curr_price = price(secret)
        diff = curr_price - price(prev)

        sequence.pop(0)
        sequence.append(diff)

        prev = secret

        tpl = tuple(sequence)

        if tpl not in done_sequences:
            add(tpl, curr_price)
            done_sequences.add(tpl)
        i += 1

max_bananas = max(map(sum, sequences.values()))
print(f"Part 2: max bananas: {max_bananas}")