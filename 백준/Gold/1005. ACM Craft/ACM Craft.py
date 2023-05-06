t = int(input())

inf = 1e9

for testcase in range(t):
    n, k = map(int, input().split())  # 건물의 개수, 규칙의 개수
    building_time = [0]+list(map(int, input().split()))  # 건물당 시간 n개
    need = [[0]]+[[] for _ in range(n)]  # 각 건물을 짓기 위한 선행조건
    time = [inf]*(n+1)  # 각 건물을 짓기 위해 필요한 최소시간    
    
    for _ in range(k):  # 각 건물 당 선행조건 넣어주기
        temp = tuple(map(int, input().split()))
        need[temp[1]].append(temp[0])
        
    w = int(input())  # 승리하기 위해 건설해야 하는 건물 번호 
          
    done = False
    i = 1
    while not done:
        if done:
            break
        max_time = 0
        for building in need[i]:  # 어떤 건물의 필요조건 중 하나에 대해
            t = time[building]  # 그 건물을 짓기 위해 필요한 시간 (아직 불가능하다면 inf)
            if t != inf:  # 이미 충족되었다면 maxtime갱신하고 pass
                max_time = max(max_time, t)
                continue
            else:  # 충족되지 않은 건물이 있다면 break, 다음 건물 확인
                break
        else:   # 모두 충족 되었다면
            time[i] = max_time + building_time[i]  # 해당 건물을 짓기 위한 최단시간 기록
            if i == w:
                print(time[i])
                done = True
            
        i = i+1 if i != n else 1  # 끝까지 왔을 경우 처음부터 건설 가능한 건물 탐색
            
            
    
    
    