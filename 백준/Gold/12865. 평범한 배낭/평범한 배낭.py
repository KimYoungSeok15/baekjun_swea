import sys
input = sys.stdin.readline
n, k = map(int, input().split())
item = [list(map(int, input().split())) for _ in range(n)]
dp = [[0,[]] for _ in range(k+1)]
for i in range(k):
    for j in range(n):
        if i+item[j][0] <= k and j not in dp[i][1] and dp[i+item[j][0]][0] < dp[i][0] + item[j][1]:
            dp[i+item[j][0]][0] = dp[i][0] + item[j][1]
            dp[i+item[j][0]][1] = dp[i][1][:] + [j]
max_ans = 0
for l in range(k+1):
    max_ans = max(max_ans, dp[l][0])
print(max_ans)