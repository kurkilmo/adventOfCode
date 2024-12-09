import time

data = open("input.txt").read().strip()

def read_memory(data):
    memory = []

    data_ind = 0
    file_ind = 0

    while data_ind < len(data):
        data_num = int(data[data_ind])

        if data_ind % 2 == 0:
            # file
            for i in range(data_num):
                memory.append(file_ind)
            file_ind += 1
        else:
            # empty
            for i in range(data_num):
                memory.append(None)
        data_ind += 1
    return memory

def defrag_part1(memory):
    size = len(memory)
    for i in range(size):
        try:
            if memory[i] != None: continue
        except IndexError:
            break
        rear_ind = -1
        while (size + rear_ind) != i:
            if memory[rear_ind] != None:
                memory[i] = memory[rear_ind]
                memory[rear_ind] = None
                break
            rear_ind -= 1

def print_memory(memory):
    res = ""
    for a in memory:
        if a == None:
            res += '.'
        else:
            res += str(a)
    print(res)

def defrag_part2(memory):
    size = len(memory)
    rear_ind = -1
    file_ind = -1
    front_ind = 0
    moved_files = set()
    while size + rear_ind > 0:
        front_ind = 0
        file_size = int(data[file_ind])
        if memory[rear_ind] in moved_files:
            file = memory[rear_ind]
            while memory[rear_ind] == None or memory[rear_ind] == file:
                rear_ind -= 1
            continue
        while front_ind < (size + rear_ind):
            for i in range(front_ind, front_ind + file_size):
                if memory[i] != None:
                    space = False
                    break
                space = True
            if space:
                moved_files.add(memory[rear_ind])
                for i in range(0, file_size):
                    memory[front_ind + i] = memory[rear_ind - i]
                    memory[rear_ind - i] = None
                break
            else:
                while memory[front_ind] == None:
                    front_ind += 1
                while memory[front_ind] != None:
                    front_ind += 1
        file = memory[rear_ind]
        while memory[rear_ind] == None or memory[rear_ind] == file:
            rear_ind -= 1
            if size + rear_ind < 0: break
        file_ind -= 2

def checksum(memory):
    checksum = 0
    for i in range(len(memory)):
        if memory[i] == None: continue
        checksum += i * memory[i]
    return checksum

t1 = time.time()
memory = read_memory(data)
defrag_part1(memory)
print("Part 1:", checksum(memory))
t2 = time.time()
print(f"Time: {round(t2 - t1, 2)} s\n")

t1 = time.time()
memory = read_memory(data)
defrag_part2(memory)
print("Part 2:", checksum(memory))
t2 = time.time()
print(f"Time: {round(t2 - t1, 2)} s\n")
