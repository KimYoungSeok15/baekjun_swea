import sys
input = sys.stdin.readline
n, k = map(int, input().split())
num = [int(input()) for _ in range(n)]
dp = [0]*(k+1)
dp[0] = 1
for i in range(n):
    j = 0
    while j + num[i] <= k:
        dp[j+num[i]] += dp[j]
        j += 1
print(dp[k])