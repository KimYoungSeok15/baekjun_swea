import sys
input = sys.stdin.readline
n = int(input())
s = []
ans = 0
for _ in range(n):
    
    # print(f'ans: {ans}')
    t = int(input())
    
    while s and s[-1][0] < t:
        ans += s.pop()[1]

    if not s:
        s.append([t, 1])
        continue
    
    if s[-1][0] == t:
        cnt = s.pop()[1]
        ans += cnt
        s.append([t, cnt+1])
        if t < s[0][0]:
            ans += 1
        continue

    s.append([t, 1])
    ans += 1
    
print(ans)