from collections import deque
from sys import stdin
input = stdin.readline
t = int(input())
for tc in range(t):
    m, n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(k)]
    board = [[0]*n for _ in range(m)] 
    visited = [[0]*n for _ in range(m)]
    d = ((0,1),(0,-1),(1,0),(-1,0))
    ans = 0
    for cab in arr:
        board[cab[0]][cab[1]] = 1
    for i in range(m):
        for j in range(n):
            if board[i][j] and not visited[i][j]:
                ans += 1
                q = deque([(i,j)])
                while q:
                    om, on = q.popleft()
                    for dm, dn in d:
                        nm, nn = om+dm, on+dn
                        if 0<=nm<m and 0<=nn<n and not visited[nm][nn] and board[nm][nn]:
                            visited[nm][nn] = 1
                            q.append((nm, nn))
    print(ans)