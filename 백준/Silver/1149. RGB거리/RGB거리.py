import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*3 for _ in range(n)]
dp[0] = arr[0]
for i in range(n-1):
    dp[i+1] = [min(dp[i][1],dp[i][2])+arr[i+1][0], min(dp[i][0],dp[i][2])+arr[i+1][1],min(dp[i][0],dp[i][1])+arr[i+1][2]]
print(min(dp[n-1]))
