def lcs_length(X, Y):
    m = len(X)
    n = len(Y)

    # 테이블 초기화
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # LCS 길이 계산
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

# 두 문자열 입력 받기
X = input().strip()
Y = input().strip()

# LCS의 길이 출력
result = lcs_length(X, Y)
print(result)