from itertools import combinations

n = int(input())
arr = [input().split() for _ in range(n)]
empty = []
teacher = []
student = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == "X":
            empty.append((i, j))
        elif arr[i][j] == "S":
            student.append((i, j))
        else:
            teacher.append((i, j))

d = ((1, 0), (0, 1), (-1, 0), (0, -1))

pos_row = set()
pos_col = set()
for t in teacher:
    pos_row.add(t[0])
    pos_col.add(t[1])

pos = set()
for pr in pos_row:
    for j in range(n):
        if arr[pr][j] == "X":
            pos.add((pr, j))

for pc in pos_col:
    for i in range(n):
        if arr[i][pc] == "X":
            pos.add((i, pc))

for case in combinations(pos, 3):
    for obs in case:
        arr[obs[0]][obs[1]] = "O"
    flag = True
    for t in teacher:
        r, c = t
        for dr, dc in d:
            for cnt in range(1, 6):
                nr, nc = r + dr * cnt, c + dc * cnt
                if 0 <= nr < n and 0 <= nc < n:
                    if arr[nr][nc] == "S":
                        flag = False
                        break
                    elif arr[nr][nc] == "O":
                        break
                    elif arr[nr][nc] == "T":
                        break
                    else:
                        continue
                else:
                    break
        if not flag:
            break

    if flag:
        print("YES")
        exit()

    for obs in case:
        arr[obs[0]][obs[1]] = "X"

print("NO")
