import sys
input = sys.stdin.readline
n, k = map(int, input().split())
coin = set()
for _ in range(n):
    coin.add(int(input()))
coin = list(coin)
dp = [0]*(k+1)
inf = int(1e9)
for i in range(len(coin)):
    if coin[i] <= k:
        dp[coin[i]] = 1
    for j in range(k-coin[i]+1):
        if dp[j] and j+coin[i]<=k:
            dp[j+coin[i]] = min(dp[j+coin[i]] if dp[j+coin[i]] else inf, dp[j]+1)
print(dp[k] if dp[k] else -1)