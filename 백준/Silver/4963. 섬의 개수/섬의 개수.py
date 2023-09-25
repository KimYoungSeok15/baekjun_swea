import sys
input = sys.stdin.readline
d = ((0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1))
while True:
  ans = 0
  t = input().split()
  if t[0] == t[1] == '0':
    exit()
  m, n = map(int, t)
  board = [list(map(int, input().split())) for _ in range(n)]
  v = [[0]*m for _ in range(n)]
  for i in range(n):
    for j in range(m):
      if not v[i][j] and board[i][j]:
        v[i][j] = 1
        s = [(i,j)]
        while s:
          r, c = s.pop()
          for dr, dc in d:
            nr, nc = r+dr, c+dc
            if 0<=nr<n and 0<=nc<m and not v[nr][nc] and board[nr][nc]:
              s.append((nr,nc))
              v[nr][nc] = 1
        ans += 1
  print(ans)