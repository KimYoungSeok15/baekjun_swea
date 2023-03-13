n, m = map(int, input().split())
lst = [input().split() for _ in range(n)]
visited = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if lst[i][j] == '2':
            q = [(i,j)]
            start_x, start_y = i, j
            break
while q:
    r, c = q.pop(0)
    dis = visited[r][c]
    for dr, dc in ((1,0),(-1,0),(0,-1),(0,1)):
        if n-1>=r+dr>=0 and m-1>=c+dc>=0 and lst[r+dr][c+dc] == '1' and not visited[r+dr][c+dc]:
            q.append((r+dr,c+dc))
            visited[r+dr][c+dc] = dis+1
for p in range(n):
    for q in range(m):
        if not visited[p][q] and lst[p][q] == '1' and not (p == start_x and q == start_y):
            visited[p][q] = -1
for k in range(n):
    print(*visited[k])
