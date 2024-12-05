lines = open("input.txt").readlines()

# Parsing
pairs = []
lines_ind = 0
while lines[lines_ind] != '\n':
    pairs.append(list(map(int,lines[lines_ind].split('|'))))
    lines_ind += 1

lines_ind += 1
updates = []
while lines_ind < len(lines):
    updates.append(list(map(int,lines[lines_ind].split(','))))
    lines_ind += 1

# Part 1
def check_update(update: list):
    for i in range(len(update)):
        for j in range(i+1, len(update)):
            if ([update[j], update[i]] in pairs):
                return False
    return True

def middle_value(update: list):
    return update[int((len(update)-1)/2)]

sum = 0
wrong_updates = []
for update in updates:
    if check_update(update):
        sum += middle_value(update)
    else: wrong_updates.append(update)

print("Part 1:", sum)

# Part 2
def sort_update(update: list):
    for i in range(len(update)):
        for j in range(i+1, len(update)):
            if [update[j], update[i]] in pairs:
                bef = update[i]
                aft = update[j]
                update.pop(i)
                update.insert(i, aft)
                update.pop(j)
                update.insert(j, bef)

sum_2 = 0
for update in wrong_updates:
    sort_update(update)
    sum_2 += middle_value(update)

print("Part 2:", sum_2)
