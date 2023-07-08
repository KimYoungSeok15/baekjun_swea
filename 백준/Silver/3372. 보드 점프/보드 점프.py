n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
dp[0][0] = 1
for i in range(2*n-2):
    for j in range(i+1):
        if 0<=i-j<n and 0<=j<n:
            if dp[i-j][j]:
                for nr, nc in ((i-j+board[i-j][j],j),(i-j,j+board[i-j][j])):
                    if 0<=nr<n and 0<=nc<n:
                        dp[nr][nc] += dp[i-j][j]
print(dp[n-1][n-1])