import sys
input = sys.stdin.readline
N = int(input())
h = [list(map(int,input().split())) for _ in range(N)]
d = [[0,0,0] for _ in range(N+1)]

for i in range(N):
    d[i+1][0] = min(d[i][1], d[i][2]) + h[i][0]
    d[i+1][1] = min(d[i][0], d[i][2]) + h[i][1]
    d[i+1][2] = min(d[i][0], d[i][1]) + h[i][2]
print(min(d[N])) 