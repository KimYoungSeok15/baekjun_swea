import sys
input = sys.stdin.readline
n, m = map(int,input().split())
ans = 0
s = {input() for _ in range(n)}
t = [input() for _ in range(m)]
for i in t:
    if i in s:
        ans += 1
print(ans)