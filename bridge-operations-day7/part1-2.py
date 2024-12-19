lines = open("input.txt").readlines()

def div(a, b):
    div, rem = divmod(a, b)
    if rem < 0:
        div += 1
        rem += abs(b)
    return (div,rem)

def convert(num:int, base:int):
    d = div(num, base)
    res = str(int(d[1]))
    while d[0] != 0:
        d = div(d[0], base)
        res = str(int(d[1])) + res
    return res

def get_operations(length):
    return [bin(i)[2:].rjust(length, "0") for i in range(2**length)]
# 1 = *     0 = +

def get_operations_concat(length):
    return [convert(i, 3).rjust(length, "0") for i in range(3**length)]

def print_operation(target, numbers, operation):
    res = f"{target} = {numbers[0]} "
    for i in range(1, len(numbers)):
        if operation[i-1] == '1': res += "* "
        elif operation[i-1] == '0': res += "+ "
        elif operation[i-1] == '2': res += "|| "
        res += f"{numbers[i]} "
    print(res)

def concat(a, b):
    return int(str(a)+str(b))

def get_sum(concatenate = False):
    possibles_sum = 0
    for line in lines:
        spl = line.split(": ")
        target = int(spl[0])
        numbers = list(map(int, spl[1].split(" ")))

        if concatenate: operations = get_operations_concat(len(numbers) - 1)
        else: operations = get_operations(len(numbers) - 1)

        for operation in operations:
            operation_result = numbers[0]
            for i in range(1, len(numbers)):
                if operation[i-1] == '1':
                    operation_result *= numbers[i]
                elif operation[i-1] == '0':
                    operation_result += numbers[i]
                elif concatenate and (operation[i-1] == '2'):
                    operation_result = concat(operation_result, numbers[i])

                if operation_result > target: break
            if operation_result == target:
                print_operation(target, numbers, operation)
                possibles_sum += target
                break
    return possibles_sum

print("Part 1:", get_sum())
print("\nPart 2:", get_sum(True))

