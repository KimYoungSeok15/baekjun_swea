import sys
input = sys.stdin.readline

n = int(input())
dots = []
ans = 0

for _ in range(n):
    x, e = map(int, input().split())
    dots.append([e-x, x+e]) # e-x와 x+e가 큰놈이 사면 작은놈들은 삼

dots.sort()

maxi = -int(1e9)-1
for _ in range(n):
    now = dots.pop()[1]
    if maxi < now:
        ans += 1
        maxi = now

print(ans)
