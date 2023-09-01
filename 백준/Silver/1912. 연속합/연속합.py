n = int(input())
arr = list(map(int, input().split()))
inf = int(-1e9)
dp = [inf]*n
dp[0] = max(0,arr[0])
for i in range(n-1):
    dp[i+1] = max(0,dp[i]+arr[i+1])
if max(arr) < 0:
    print(max(arr))
    exit()
print(max(dp))