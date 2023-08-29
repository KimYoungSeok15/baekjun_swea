n = int(input())

if n == 1:
    print(1)

arr = list(map(int, input().split()))
inf = int(1e9)
dp = [inf]*n
dp[0] = 0
for i in range(n):
    for j in range(n-1):
        if dp[j] != inf and dp[j] < arr[i]:
            dp[j+1] = min(dp[j+1], arr[i])
        else:
            break
p = 0

while p<n:
    if dp[p] == inf:
        print(p-1)
        exit()
    p += 1
