lines = open("input.txt").readlines()
sequences = []
for l in lines:
    l = l.strip()
    sequences.append(l.split(" "))
for i in range(len(sequences)):
    for j in range(len(sequences[i])):
        sequences[i][j] = int(sequences[i][j])
    
def is_zero(l:list):
    for a in l:
        if a != 0:
            return False
    return True
    
def predict_part1(seq:list):
    diff = []
    i = 1
    while i < len(seq):
        dif = (seq[i] - seq[i-1])
        diff.append(dif)
        i += 1
    if is_zero(diff):
        return 0
    res = diff[-1] + predict_part1(diff)
    return res

def predict_part2(seq:list):
    diff = []
    i = 1
    while i < len(seq):
        dif = (seq[i] - seq[i-1])
        diff.append(dif)
        i += 1
    if is_zero(diff):
        return 0
    res = diff[0] - predict_part2(diff)
    return res
    
def main():
    sum_p1 = 0
    sum_p2 = 0
    for seq in sequences:
        print(seq)
        pred_p1 = seq[-1] + predict_part1(seq)
        pred_p2 = seq[0] - predict_part2(seq)
        sum_p1 += pred_p1
        sum_p2 += pred_p2
        print(f'sequence: {seq}, prediction part 1: {pred_p1}, prediction part 2: {pred_p2}')
    print(f'Part 1: Sum: {sum_p1}')
    print(f'Part 2: Sum: {sum_p2}')
    
if __name__ == "__main__":
    main()