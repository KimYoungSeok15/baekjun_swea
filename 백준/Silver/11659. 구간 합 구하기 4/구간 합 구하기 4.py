import sys
input = sys.stdin.readline
n, m = map(int,input().split())
arr = list(map(int, input().split()))
dp = [0]*n
dp[0] = arr[0]
for i in range(1,n):
  dp[i] = dp[i-1] + arr[i]
ij = [list(map(int, input().split())) for _ in range(m)]
for i in ij:
  print(dp[i[1]-1]-(dp[i[0]-2] if i[0]-2>=0 else 0))
