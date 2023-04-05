m, n = map(int, input().split())
lst = [list(map(int, list(input()))) for _ in range(m)]
visited = [[0]*n for _ in range(m)]
d = ((1,0),(0,1),(-1,0),(0,-1))
for i in range(n):
    if lst[0][i]:
        continue
    s = [[0,i]]
    while s:
        r, c = s.pop()
        visited[r][c] = 1
        for dr, dc in d:
            if 0<=r+dr<=m-1 and 0<=c+dc<=n-1 and not visited[r+dr][c+dc] and not lst[r+dr][c+dc]:
                if r+dr == m-1:
                    print('YES')
                    exit()
                s.append([r+dr, c+dc])
print('NO')