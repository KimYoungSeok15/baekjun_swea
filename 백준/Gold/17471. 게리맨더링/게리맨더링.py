def dfs(x):  # x번째 구역에서 dfs실행하여 조건에 맞지 않다면 False를 return하는 함수
    global a_searched, b_searched
    in_a = True if x in subset_A else False  # 현재 선거구가 a라면 True, 아니라면 False

    if in_a and a_searched:  # 이미 이전에 a선거구 지역들을 dfs했을 경우(연결되어 있지 않는 구역일 경우)
        return False
    elif not in_a and b_searched:
        return False

    visited[x] = 1  # 방문 처리
    for connected in range(1, info[x][0]+2):  # 연결된 지역들에 대해 dfs 실행
        if in_a and info[x][connected] in subset_A and not visited[info[x][connected]] :  # 현재 선거구에 속한 미방문 지역이면
            dfs(info[x][connected])  # dfs 실행
        elif not in_a and info[x][connected] in subset_B and not visited[info[x][connected]] :  # 현재 선거구에 속한 미방문 지역이면
            dfs(info[x][connected])  # dfs 실행     
  
    return True  # 이상 없음
    
n = int(input())  # 구역 수
pop = list(map(int, input().split()))  # 인구
info = [list(map(lambda x: int(x)-1, input().split())) for _ in range(n)]  # 각 구역에 연결된 구역들
ans = 1000  # 최소 인구차이. 최대 999까지 가능
for i in range(1<<n):  # 2**n의 경우의 수에 대해
    subset_A, subset_B = set(), set()  # A 선거구 지역들      
    for j in range(n):  # j: 부분집합 생성 시 이진법의 각 자리수 비교용. 아래부터는 특정 부분집합에 대해 조사
        subset_A.add(j) if i&1<<j else subset_B.add(j) # 1일 경우 A 선거구, 0일 경우 B 선거구
    if len(subset_A)< n//2 or len(subset_A) == n:  # A 와 B가 반전됐을 때도 같은 상황이므로 넘어가고, 공집합도 제거
        continue
    a_searched, b_searched = False, False  # 각 선거구를 dfs 했는지 (떨어져 있는 지역 있는지) 확인용    
    visited = [0]*n  # 방문 확인용
    flag = True  # 계속 진행할지 확인용
    # a 구역 탐색
    for a in subset_A:
        if not visited[a]:
            if dfs(a) == True:
                a_searched = True  # 미방문지역 dfs해서 False가 나왔다면
            else:
                flag = False  
                break
    if flag == False: # 다음걸로 넘어가자
        continue
    # b 구역 탐색
    for b in subset_B:
        if not visited[b]:
            if dfs(b) == True:
                b_searched = True  # 미방문지역 dfs해서 False가 나왔다면
            else:
                flag = False  
                break
    if flag == False: # 다음걸로 넘어가자
        continue
    # 유효한 상황이라면 인구계산
    temp = 0
    for a in subset_A:
        temp += pop[a]
    for b in subset_B:
        temp -= pop[b]
    # print(subset_A, subset_B, temp)
    ans = min(ans, abs(temp))
print(-1) if ans == 1000 else print(ans) 