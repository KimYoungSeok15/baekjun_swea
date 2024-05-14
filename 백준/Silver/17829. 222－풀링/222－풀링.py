import sys

input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
while N > 1:
    N //= 2
    n_arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            n_arr[i][j] = sorted(
                [
                    arr[i * 2][j * 2],
                    arr[i * 2][j * 2 + 1],
                    arr[i * 2 + 1][j * 2],
                    arr[i * 2 + 1][j * 2 + 1],
                ]
            )[2]
    arr = n_arr
print(arr[0][0])
