n = int(input())
arr = list(map(int, input().split()))
# 인덱스가 최대값, 값이 길이
dp = [0]*(1001)
for i in range(n):
    dp[arr[i]] = max(dp[arr[i]], 1)
    for j in range(arr[i]+1, 1001):
        dp[arr[i]] = max(dp[arr[i]], dp[j]+1)
print(max(dp))