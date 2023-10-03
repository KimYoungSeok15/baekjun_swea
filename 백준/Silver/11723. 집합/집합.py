import sys
input = sys.stdin.readline
s = set()
n = int(input())
for _ in range(n):
    t = input().split()
    if len(t) > 1:
        t[1] = int(t[1])
    if t[0] == 'add':
        s.add(t[1])
    elif t[0] == 'remove':
        try:
            s.remove(t[1])
        except:
            pass
    elif t[0] == 'check':
        if t[1] in s:
            print(1)
        else:
            print(0)
    elif t[0] == 'toggle':
        try:
            s.remove(t[1])
        except:
            s.add(t[1])
    elif t[0] == 'all':
        s = set(range(1,21))
    else:
        s = set()
