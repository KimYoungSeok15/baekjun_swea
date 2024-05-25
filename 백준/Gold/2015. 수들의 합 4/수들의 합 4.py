N, K = map(int, input().split())
arr = list(map(int, input().split()))

# 누적합을 저장할 딕셔너리. 0은 누적합의 초기값.
d = {0: 1}
s = 0
ans = 0

for i in range(N):
    s += arr[i]
    
    # 합이 K인 부분합의 개수를 누적합에서 찾음
    if s - K in d:
        ans += d[s - K]

    # 현재 누적합을 딕셔너리에 추가 또는 증가시킴
    if s in d:
        d[s] += 1
    else:
        d[s] = 1

print(ans)
