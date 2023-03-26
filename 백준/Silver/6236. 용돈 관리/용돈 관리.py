n, m = map(int , input().split())
spend = [int(input()) for _ in range(n)]
s = max(spend)  # 가장 큰 지출 = 최소한의 인출 값
e = s * n  # 최대 인출 값
while not s == e:  # 찾기 전까지
    mid = (s+e) // 2  # 중간 값. 1회당 인출 비용.
    temp = mid  # 현재 보유 캐쉬
    cnt = 1  # 총 인출 횟수
    for i in range(n):  # 모든 날에 대해 최소 몇번의 인출이 필요한지 계산
        if temp < spend[i]:  # 보유 캐쉬가 부족하다면
            temp = mid - spend[i]  # 보유 캐쉬 반납 후 캐쉬 충전 후 잔액
            cnt += 1  # 인출 횟수 증가
        else:  # 보유 캐쉬가 충분하다면
            temp -= spend[i]
    if cnt > m:  # 너무 잦은 인출이라면
        s = mid + 1  # 더 큰 비용을 인출해보자
    else:  # 너무 뜸한 인출이거나 m을 찾았다면
        e = mid # 가능한 더 작은 비용을 인출해보자
print(s)
