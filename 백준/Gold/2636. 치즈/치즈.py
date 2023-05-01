from collections import deque
r, c = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(r)]
visited = [[False]*c for _ in range(r)]
cnt = 0  # 총 방문 횟수
ans1, ans2 = 0, 0  # 시간 / 마지막 남은 치즈 수
q = deque([(0,0)])
while True:  # 다 녹기 전까지 실행   
    cheese = deque([])  # 녹을 예정인 치즈      
    while q:
        y, x = q.popleft()
        # if not visited[y][x] == True:  # 방문처리
        #     visited[y][x] = True
        #     cnt += 1
        # 델타탐색
        for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
            if 0<=y+dy<=r-1 and 0<=x+dx<=c-1 and not visited[y+dy][x+dx]:
                if m[y+dy][x+dx]:  # 공기에 접촉된 치즈라면
                    visited[y+dy][x+dx] = True
                    cnt += 1                    
                    cheese.append((y+dy, x+dx))
                else:  # 공기라면
                    q.append((y+dy, x+dx))
                    visited[y+dy][x+dx] = True
                    cnt += 1                      
    q.extend(cheese)
    if not cheese:
        break
    ans2 = len(cheese)
    ans1 += 1

print(ans1)
print(ans2)
