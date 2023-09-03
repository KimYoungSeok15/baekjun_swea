n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
for row in range(n):  # 상어 시작점 r,c에 저장
    for col in range(n):
        if lst[row][col] == 9:
            r, c = row, col
            lst[row][col] = 0
size = 2
exp = 0  # 경험치
dist = 0 # 이동한 총 거리
while True:
    t_list = []  # 타겟 리스트
    # bfs. 현재 위치에서 갈 수 잇는 타겟을 정하는 과정
    q = [[r, c]]    
    visited = [[0]*n for _ in range(n)] 
    while q:
        temp = q.pop(0)
        row, col = temp[0], temp[1]
        if lst[row][col] and lst[row][col] < size:  # 현재 위치에 물고기가 있고 현재 사이즈보다 작다면
            if not t_list or t_list[0][2] == visited[row][col]:  # 타겟 리스트가 비었거나 타겟 리스트들의 거리가 현재 거리와 같다면
                t_list.append([row, col, visited[row][col]])  # 타겟 행, 열, 거리 저장          
        if row < n-1 and not visited[row+1][col] and lst[row+1][col] <= size:
            q.append([row+1, col])
            visited[row+1][col] = visited[row][col] + 1 
        if row > 0 and not visited[row-1][col] and lst[row-1][col] <= size:
            q.append([row-1, col]) 
            visited[row-1][col] = visited[row][col] + 1
        if col < n-1 and not visited[row][col+1] and lst[row][col+1] <= size:
            q.append([row, col+1])
            visited[row][col+1] = visited[row][col] + 1
        if col > 0 and not visited[row][col-1] and lst[row][col-1] <= size:
            q.append([row, col-1]) 
            visited[row][col-1] = visited[row][col] + 1
    if not t_list:  # 타겟이 없다면
        break
    if len(t_list) > 1:  # 거리가 같은 것이 여러개면
        prior = [20,20]
        for fish in t_list:
            if fish[0]<prior[0]:  # 가장 위에 있는 것 저장
                prior = [fish[0], fish[1]]
            elif fish[0] == prior[0] and fish[1] < prior[1]:  #  행이 같다면 열이 적은 것을 타겟으로
                prior = [fish[0], fish[1]]
        r, c = prior[0], prior[1]  # 이동
        lst[r][c] = 0            
    else:  # 타겟이 하나면
        r, c = t_list[0][0], t_list[0][1]  # 이동
        lst[r][c] = 0         
    dist += t_list[0][2]  # 이동 거리 증가
    exp += 1  # 경험치 추가, 레벨업 확인
    if exp == size:
        size += 1
        exp = 0                 
print(dist)