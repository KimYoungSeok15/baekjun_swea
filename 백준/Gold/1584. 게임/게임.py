from collections import deque
n = int(input())
danger = [list(map(int,input().split())) for _ in range(n)]
m = int(input())
death = [list(map(int,input().split())) for _ in range(m)]
inf = 2<<13
visited = [[inf]*501 for _ in range(501)]
visited[0][0] = 0
d = ((0,1),(1,0),(-1,0),(0,-1))
q = deque([(0,0)])
while q:
    x, y = q.popleft()
    for dx, dy in d:
        if 0<=x+dx<=500 and 0<=y+dy<=500:  # 경기장 이탈방지
            for D in death:   # 갈 수 없는 지역인지
                if min(D[0],D[2]) <= x+dx <= max(D[0],D[2]) and min(D[1],D[3]) <= y+dy <= max(D[1],D[3]):
                    break
            else:  # 갈 수 있다면
                for dan in danger:  # 위험지역 확인
                    if min(dan[0],dan[2]) <= x+dx <= max(dan[0],dan[2]) and min(dan[1],dan[3]) <= y+dy <= max(dan[1],dan[3]):
                        if visited[x+dx][y+dy] > visited[x][y] + 1:  # 갱신 가능하면 갱신 후 다시 bfs
                            visited[x+dx][y+dy] = visited[x][y] + 1
                            q.append((x+dx,y+dy))
                        break  # 위험지역이면서 갱신 불가능 하면 pass
                else:  # 위험지역이 아니면
                    if visited[x+dx][y+dy] > visited[x][y]:  # 갱신 가능하면 갱신 후 다시 bfs
                        visited[x+dx][y+dy] = visited[x][y]
                        q.append((x+dx,y+dy))                      
print(visited[500][500] if visited[500][500] != inf else -1)                    