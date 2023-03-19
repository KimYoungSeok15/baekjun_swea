t= int(input())
for _ in range(t):
    n = int(input())
    dp = [[0,1,0],[0,0,1]] + [[0,0,0]] * (n-1)
    zero = 1
    one = 1
    for i in range(2,n+1):
        dp[i] = [dp[i-2][0] + dp[i-1][0], dp[i-2][1] + dp[i-1][1], dp[i-2][2] +dp[i-1][2]]
    print(dp[n][1],dp[n][2])
        