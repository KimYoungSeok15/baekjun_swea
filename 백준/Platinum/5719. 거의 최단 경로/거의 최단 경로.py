import heapq
import sys
from collections import deque
input = sys.stdin.readline

def step(now, dis, q, v):
    for e in edge[now]:
        if v[e[0]] > dis + e[1] and not dropped[now][e[0]]:  # 갱신 가능한 경우
            v[e[0]] = dis + e[1]
            heapq.heappush(q, (dis+e[1], e[0]))

        
while True:
    no, ed = map(int, input().split())
    if no == ed == 0:
        exit()
    st, en = map(int, input().split())

    edge = [[] for _ in range(no)]  # 가는쪽 입장
    rev_edge = [[] for _ in range(no)]  # 오는쪽 입장
    
    for _ in range(ed):
        u, v, p = map(int, input().split())
        edge[u].append((v, p)) # u에서 v로 가는 비용이 p다
        rev_edge[v].append((u, p))  # 마찬가지
    
    inf = int(1e9)
    v = [inf]*no
    dropped = [[False]*no for _ in range(no)]
    
    def dijkstra():
        q = [(0, st)]
        while q:
            dis, now = heapq.heappop(q)
            
            if v[now] < dis:  # 이미 갱신된 자료인 경우
                continue

            v[now] = dis
            step(now, dis, q, v)

        return v[en]
    
    best = dijkstra()
    
    # 끝점부터 bfs. 최단거리에 해당하는 경우에만 탐색. 탐색과 동시에
    # 해당 엣지 삭제.
    deq = deque([en])
    while deq:
        now = deq.popleft()
        dis = v[now]
        for e in rev_edge[now]:
            if dis-e[1] == v[e[0]] and not dropped[e[0]][now]:
                deq.append(e[0])
                dropped[e[0]][now] = True
    
    v = [inf]*no 
    ans = dijkstra()
    
    print(ans if ans != inf else -1)
    
    
