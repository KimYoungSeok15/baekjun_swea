import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
dp = [0]*(max(max(arr)+1, 10))
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4,max(arr)+1):
    dp[i] = dp[i-3]% 1000000009 + dp[i-2]% 1000000009 + dp[i-1]% 1000000009
for j in arr:
    print(dp[j]%1000000009)