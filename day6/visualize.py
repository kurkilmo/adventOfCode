import sys

def insert_string(s: str):
    lines = s.split('\n')
    #lines.reverse()
    sys.stdout.write('\33[A' * len(lines))
    for line in lines:
        sys.stdout.write(line + '\n')
    sys.stdout.flush()

def visualize(size, obstacles, guard, guard_dir, new, visited):
    res = ""
    for i in range(size):
        for j in range(size):
            if [i,j] in obstacles:
                res += "#"
            elif [i,j] in new:
                res += "O"
            elif guard == [i,j]:
                res += "^>v<"[guard_dir]
            
            else: res += visited[i][j]
        res += "\n"
    return res
