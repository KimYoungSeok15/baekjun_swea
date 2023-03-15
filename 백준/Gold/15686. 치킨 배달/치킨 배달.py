# 정보 저장 구간
n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
chicken_lst = []  # 치킨집 위치 저장
house_lst = []  # 집 위치 저장
m_chicken_lst = []  # 치킨집들 중 m개 치킨집을 갖는 부분집합 생성
distances = []  # 각 집에서부터 m개의 치킨집들로 부터의 최소 거리의 합들을 저장

for i in range(n): # 치킨집, 집 저장
    for j in range(n):
        if lst[i][j] == 1:
            house_lst.append([i,j])
        elif lst[i][j] == 2:
            chicken_lst.append([i,j])


# 길이 m인 부분집합 생성
for j in range(1<<len(chicken_lst)):
    temp = []
    for k in range(len(chicken_lst)):
        if j & 1<<k:
            temp.append(k)
    if len(temp) == m:
        m_chicken_lst.append([chicken_lst[l] for l in temp])

# 부분집합들에 대해 거리 계산
for chickens in m_chicken_lst:  # m개의 부분집합 중에서 하나를 고른다.
    chick_sum = 0  # 그 부분집합의 총 거리
    for house in house_lst:  # 각 집에 대해
        house_sum = []   # 그 집으로 부터 
        for chick in chickens: # 치킨집들까지의 거리들을 저장
            house_sum.append(abs(chick[0]-house[0]) + abs(chick[1]-house[1]))
        chick_sum += min(house_sum)  # 각 치킨집들과의 거리 중 최솟값만 부분집합의 결과에 더해준다.
    distances.append(chick_sum)  # 어떤 부분집합의 결과를 distance에 저장

# 최소 거리 출력
print(min(distances))  # 각 부분집합의 결과 중 가장 최솟값을 출력