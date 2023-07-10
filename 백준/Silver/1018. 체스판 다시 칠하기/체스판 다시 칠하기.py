n, m = map(int, input().split())
board = [input() for _ in range(n)]
ans = int(1e9)
for i in range(n-7):
    for j in range(m-7):
        temp = 0
        for k in range(8):
            for l in range(8):
                if (k+l)%2:
                    if board[i+k][j+l] == 'W':
                        temp += 1
                else:
                    if board[i+k][j+l] == 'B':
                        temp += 1
        ans = min(ans, temp, 64-temp)
print(ans)