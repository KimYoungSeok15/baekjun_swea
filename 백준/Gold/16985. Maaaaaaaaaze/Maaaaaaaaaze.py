from itertools import permutations
from collections import deque
arr = [[[list(map(int, input().split())) for _ in range(5)]] for _ in range(5)]
def bfs():
    global ans
    visited = [[[0]*5 for _ in range(5)] for _ in range(5)]
    start = [0,0,0,0]
    delta = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
    visited[0][0][0] = 1
    q = deque([start])
    while q:
        h,r,c,dis = q.popleft()
        if h==4 and r==4 and c==4:
            return dis
        if dis > ans:
            continue
        for dh, dr, dc in delta:
            nh, nr, nc = h+dh, r+dr, c+dc
            if (0<=nh<=4 and 0<=nr<=4 and 0<=nc<=4) and not visited[nh][nr][nc] and temp[nh][nr][nc]:
                q.append([nh,nr,nc,dis+1])
                visited[nh][nr][nc] = dis+1
    return 50
ans = 50
for j in range(5):
    for i in range(3):
        arr[j].append([[arr[j][i][4-c][r] for c in range(5)] for r in range(5)])
for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                for e in range(4):
                    for temp in permutations([arr[0][a],arr[1][b],arr[2][c],arr[3][d],arr[4][e]], 5): 
                        if not temp[0][0][0]:
                            continue
                        ans = min(bfs(), ans)
                        if ans == 12:
                            print(12)
                            exit()
print(ans if ans != 50 else -1)


