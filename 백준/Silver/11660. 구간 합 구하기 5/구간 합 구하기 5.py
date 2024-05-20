import sys
input = sys.stdin.readline
print = sys.stdout.write
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
s = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(N):
    for j in range(N):
        s[i + 1][j + 1] = s[i][j + 1] + s[i + 1][j] + arr[i][j] - s[i][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(str(s[x2][y2] - s[x2][y1 - 1] - s[x1 - 1][y2] + s[x1 - 1][y1 - 1]) + "\n")
