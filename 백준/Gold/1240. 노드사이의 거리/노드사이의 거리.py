from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
edge = [[] for _ in range(n+1)]

for _ in range(n-1):
    p, q, r = map(int, input().split())
    edge[p].append([q,r])
    edge[q].append([p,r])
    
find = [list(map(int, input().split())) for _ in range(m)]

for a, b in find:
    q = deque([a])
    visited = [0]*(n+1)
    
    while q:
        
        now = q.popleft()
        for e in edge[now]:
            if not visited[e[0]]:
                visited[e[0]] = visited[now] + e[1]
                q.append(e[0])   
                             
                if e[0] == b:
                    print(visited[b])
                    q = []
                    break