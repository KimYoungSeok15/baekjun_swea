n = int(input())
ans = 0
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0,0,0] for __ in range(n)] for _ in range(n)]
dp[0][1][0] = 1
for i in range(2*n-2):
    for j in range(i+1):
        if j < n and i-j < n and not board[j][i-j]:
            if i-j+1<n and not board[j][i-j+1]:
                dp[j][i-j+1][0] += dp[j][i-j][0] + dp[j][i-j][1]
            if j+1 < n and i-j+1 < n and not board[j+1][i-j+1] and not board[j][i-j+1] and not board[j+1][i-j]:
                dp[j+1][i-j+1][1] += sum(dp[j][i-j])
            if j+1<n and not board[j+1][i-j]:
                dp[j+1][i-j][2] += dp[j][i-j][1] + dp[j][i-j][2]
                
print(sum(dp[n-1][n-1]))