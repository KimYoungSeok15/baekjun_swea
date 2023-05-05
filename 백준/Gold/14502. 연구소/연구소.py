from itertools import combinations
from collections import deque
from copy import deepcopy
n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
virus = []
paths = []
delta = ((1,0),(-1,0),(0,1),(0,-1))

for i in range(n):
    for j in range(m):
        if lst[i][j] == 2:
            virus.append((i,j))
        elif lst[i][j] == 0:
            paths.append((i,j))

org_map = deepcopy(lst)  # 원래 맵 상태 기억

best_ans = 0  # 정답 (안전영역 최대값)

temp = 0
for wall_reset_case in combinations(paths, 3):  # 통로 중 3개를 골라 벽을 세우고, 세우는 경우마다 bfs 진행
    lst = deepcopy(org_map)  # 기존 맵으로 복구

    # 벽을 세움
    for wall in wall_reset_case:
        lst[wall[0]][wall[1]] = 1
    
    visited = [[False]*m for _ in range(n)]
    q = deque(virus)  # bfs 돌 queue 선언, 초기 virus 위치 큐에 추가

    while q:  # bfs
        r, c = q.popleft()
        lst[r][c] = 2
        for dr, dc in delta:
            nr, nc = r+dr, c+dc
            if 0<=nr<n and 0<=nc<m and not visited[nr][nc] and not lst[nr][nc]:
                q.append((nr,nc))
                visited[nr][nc] = True

    cnt = 0
    for i in range(n):
        for j in range(m):
            if lst[i][j] == 0:
                cnt += 1
    
    best_ans = max(best_ans, cnt)
print(best_ans)