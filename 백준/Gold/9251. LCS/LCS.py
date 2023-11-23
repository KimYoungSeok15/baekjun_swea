a = input()
b = input()
inf = -int(1e9)
dp = [[0] * (len(a)+1) for _ in range(len(b)+1)]

# 첫 번째 행 초기화
for i in range(len(a)):
    if a[i] == b[0]:
        dp[1][i+1:] = [1] * (len(a) - i)
        break

# 첫 번째 열 초기화
for j in range(len(b)):
    if a[0] == b[j]:
        dp[j+1][1] = 1

# LCS 길이 계산
for i in range(1, len(b)+1):
    for j in range(1, len(a)+1):
        if a[j-1] == b[i-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(b)][len(a)])