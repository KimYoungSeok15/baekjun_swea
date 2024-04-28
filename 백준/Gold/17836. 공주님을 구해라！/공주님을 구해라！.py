import sys
from collections import deque

input = sys.stdin.readline

queue = deque()

n, m, t = map(int, input().split())

castle = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

queue.append([0, 0])
visited[0][0] = True
res = 0
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = dx[i] + x, dy[i] + y
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == False:
                if castle[nx][ny] == 2:
                    res = castle[x][y] + 1 + (n - nx - 1) + (m - ny - 1)
                if castle[nx][ny] != 1:
                    castle[nx][ny] = castle[x][y] + 1
                    queue.append([nx, ny])
                    visited[nx][ny] = True

if castle[n - 1][m - 1]:
    res = min(res, castle[n - 1][m - 1])

if res > t or res == 0:
    print("Fail")
else:
    print(res)
