n = int(input())
i = 0
dp=[0]*(n+1)
dp[0], dp[1] = 1, 1
if n>=2:
    dp[2] = 2
while i < n-2:
    dp[i+3] = dp[i+1]*2 + dp[i]
    i += 1
print(dp[n]%10007)