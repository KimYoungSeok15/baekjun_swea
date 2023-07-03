import sys
from collections import deque
input = sys.stdin.readline
m, n, h = map(int, input().split())
board = []
tomato = deque([])
d = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
for i in range(h):
    row = []
    for j in range(n):
        temp = list(map(int, input().split()))
        row.append(temp)
        for k in range(m):
            if temp[k] == 1:
                tomato.append((i,j,k))  # 층, 행, 열
    board.append(row)
while tomato:
    s, i, r = tomato.popleft()
    now = board[s][i][r]
    for ds, di, dr in d:
        ns, ni, nr = s+ds, i+di, r+dr
        if 0<=ns<h and 0<=ni<n and 0<=nr<m and not board[ns][ni][nr]:
            board[ns][ni][nr] = now + 1
            tomato.append((ns,ni,nr))
            
ans = 0            
for i in range(h):
    for j in range(n):
        for k in range(m):
            now = board[i][j][k]
            if not now:
                print(-1)
                exit()
            ans = max(ans, now)
print(ans-1)
            