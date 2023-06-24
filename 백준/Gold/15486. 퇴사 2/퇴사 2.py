import sys
input = sys.stdin.readline
n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]
dp = [0]*(n+1)
for day in range(n):
    if day > 0:
        dp[day] = max(dp[day-1], dp[day])
    if day + schedule[day][0] > n:
        continue
    elif dp[day+schedule[day][0]] < dp[day] + schedule[day][1]:
        dp[day+schedule[day][0]] = dp[day] + schedule[day][1]
        dp[day+schedule[day][0]]
print(max(dp))