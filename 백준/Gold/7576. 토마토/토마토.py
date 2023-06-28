import sys
from collections import deque
input = sys.stdin.readline
m, n = map(int, input().split())

board = []
q = deque([])
visited = [[0]*m for _ in range(n)]
d = ((0,1),(1,0),(-1,0),(0,-1))


for row in range(n):
    temp = list(map(int, input().split()))
    board.append(temp)
    for col in range(m):
        if temp[col] == 1:
            q.append([row,col])

while q:
    r, c = q.popleft()
    now = visited[r][c]
    for dr, dc in d:
        nr, nc = r+dr, c+dc
        if 0<=nr<n and 0<=nc<m and board[nr][nc] == 0 and not visited[nr][nc]:
            visited[nr][nc] = now + 1
            q.append([nr,nc])
                
best = 0    

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            temp = visited[i][j]
            if not temp:
                print(-1)
                exit()
            else:
                best = max(best, temp)
                
print(best)