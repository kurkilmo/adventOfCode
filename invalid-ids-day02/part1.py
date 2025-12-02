import sys

filename = "input.txt"
if len(sys.argv) >= 2:
    filename = sys.argv[1]

ranges = open(filename).read().strip().split(",")

result_p1 = 0
result_p2 = 0

for id_range in ranges:
    (start, end) = map(int, id_range.split("-"))
    for ID in range(start, end+1):
        ID_str = str(ID)
        midp = len(ID_str) // 2

        # Part 1: check if start and end halves are equal
        if ID_str[0:midp] == ID_str[midp:]:
            result_p1 += ID
        
        # Part 2: check all "splits" from 1 to half of id length
        for i in range(1, midp+1):
            parts = set()

            for j in range(0, len(ID_str), i):
                parts.add(ID_str[j:j+i])
                if len(parts) > 1: break
            
            if len(parts) == 1:
                result_p2 += ID
                break


print("Part 1 result:")
print(result_p1)

print("Part 2 result:")
print(result_p2)