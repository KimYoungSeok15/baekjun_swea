n = int(input())
arr = list(map(int, input().split()))
dp = [0]*1001
for i in range(n):
    now = arr[i]
    for j in range(now):
        dp[now] = max(dp[now], dp[j] + now)
print(max(dp))