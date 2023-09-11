n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [0]*(n+6)
i = 0
while i < n:
  j = i
  if j + arr[i][0] <= n and dp[j] + arr[i][1] > dp[j+arr[i][0]]:
    dp[j+arr[i][0]] = dp[j] + arr[i][1]
    k = j+arr[i][0]
    while k <= n:
      dp[k] = max(dp[k], dp[j] + arr[i][1])
      k += 1
  i += 1
print(max(dp))
  