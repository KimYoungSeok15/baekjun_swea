from collections import deque
n = int(input())

board = [input() for _ in range(n)]
q = deque([])
visited_normal = [[0]*n for _ in range(n)]
visited_color = [[0]*n for _ in range(n)]
d = ((0,1),(1,0),(-1,0),(0,-1))
ans_normal = ans_color = 0

for i in range(n):
    for j in range(n):
        
        if not visited_normal[i][j]:
            ans_normal += 1
            q = deque([[i,j]])
            visited_normal[i][j] = 1
            while q:
                r, c = q.popleft()
                now = board[r][c]
                for dr, dc in d:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<n and 0<=nc<n and board[nr][nc] == now and not visited_normal[nr][nc]:
                        visited_normal[nr][nc] = 1
                        q.append([nr,nc])
        
        if not visited_color[i][j]:
            ans_color += 1
            q = deque([[i,j]])
            visited_color[i][j] = 1
            while q:
                r, c = q.popleft()
                now = 'R' if board[r][c] in ('R','G') else 'B'
                for dr, dc in d:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<n and 0<=nc<n and (board[nr][nc] in ('R','G') if now == 'R' else board[nr][nc] == 'B') and not visited_color[nr][nc]:
                        visited_color[nr][nc] = 1
                        q.append([nr,nc])

print(ans_normal, ans_color)