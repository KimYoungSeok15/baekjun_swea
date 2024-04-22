N, M = map(int, input().split())
arr = []
islands = []
ans = []
d = ((1, 0), (0, 1), (-1, 0), (0, -1))


for i in range(N):
    t = input()
    arr.append(t)
    for j in range(M):
        if t[j] == "X":
            islands.append((i, j))

for r, c in islands:
    cnt = 0
    for dr, dc in d:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == "X":
            cnt += 1

    if cnt >= 2:
        ans.append((r, c))

row_min, col_min = N, M
row_max, col_max = 0, 0
board = [["."] * M for _ in range(N)]
for r, c in ans:
    row_max, col_max = max(row_max, r), max(col_max, c)
    row_min, col_min = min(row_min, r), min(col_min, c)
    board[r][c] = "X"

for row in range(row_min, row_max + 1):
    print("".join(board[row][col_min : col_max + 1]))
