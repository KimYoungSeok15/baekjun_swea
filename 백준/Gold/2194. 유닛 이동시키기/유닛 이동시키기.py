from collections import deque
import sys
input = sys.stdin.readline

n, m, a, b, k = map(int, input().split())
obs = [list(map(lambda x:int(x)-1, input().split())) for _ in range(k)]
start_r, start_c = map(lambda x: int(x)-1, input().split())
end_r, end_c = map(lambda x: int(x)-1, input().split())
d = ((1,0),(0,1),(-1,0),(0,-1))
visited = [[0]*m for _ in range(n)]
q = deque([(start_r,start_c)])

while q:
    r, c = q.popleft()
    for dr, dc in d:
        if 0<= r+dr <n-a+1 and 0<= c+dc <m-b+1 and not visited[r+dr][c+dc]:
            for o in obs:
                if r+dr <= o[0] <= r+dr+a-1 and c+dc <= o[1] <= c+dc+b-1:
                    break
            else:
                visited[r+dr][c+dc] = visited[r][c] + 1
                q.append((r+dr,c+dc))
print(visited[end_r][end_c] if visited[end_r][end_c] else -1)