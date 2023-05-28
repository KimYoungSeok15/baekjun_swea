from collections import deque
n, k = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())
d = ((0,1),(0,-1),(1,0),(-1,0))

virus = []
for i in range(n):
    for j in range(n):
        if lst[i][j]:
            virus.append((i,j,lst[i][j],0))  # 행, 열, 바이러스 번호, 현재 시간
virus.sort(key=lambda x:x[2])  # 바이러스 번호 순으로 오름차순 정렬

q = deque([i for i in virus])  # bfs용 큐

while q:  # bfs
    r, c, num, time = q.popleft()
    if time == s:  # 시간 절약 용 s초 동안만 진행 후 종료
        break
    for dr, dc in d:  # 델타탐색
        nr, nc = r+dr, c+dc
        if 0 <= nr < n and 0 <= nc < n and not lst[nr][nc]:
            q.append((nr, nc, num, time+1))
            lst[nr][nc] = num
    
print(lst[x-1][y-1])