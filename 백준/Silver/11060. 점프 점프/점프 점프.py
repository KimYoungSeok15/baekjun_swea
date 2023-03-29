n = int(input())
num = [0] + list(map(int, input().split()))
dp = [0, 1]+[1000]*(n-1)  # 인덱스가 좌표가 되도록, 시작점은 1
i = 1
while i<n:
    if dp[i]:
        for move in range(1, num[i]+1):  # 현재 위치에서 점프 가능한 곳들을 +1 해준다. 
            if i+move <= n:
                dp[i+move] = min(dp[i+move], dp[i]+1)
    i += 1
if dp[n]==1000:
    print(-1)    
else:
    print(dp[n]-1)