import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [input().rstrip() for _ in range(n)]
dp = [[0]*m for _ in range(n)]
ans = 0

# 1열 초기화
for row in range(n):
    if arr[row][0] == '1':
        dp[row][0] = 1
        ans = 1
        
# 1행 초기화        
for col in range(m):
    if arr[0][col] == '1':
        dp[0][col] = 1
        ans = 1
        
for i in range(1, n):
    for j in range(1, m):
        if arr[i][j]=='1':
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1
            ans = max(ans, dp[i][j])

print(ans**2)