import sys
input = sys.stdin.readline
n = int(input())
ans = 0
for _ in range(n):
    s = []
    word = input().rstrip()
    for i in word:
        if not s:
            s.append(i)
        elif s[-1] == i:
            s.pop()
            continue
        else:
            s.append(i)
    if not s:
        ans += 1
print(ans)