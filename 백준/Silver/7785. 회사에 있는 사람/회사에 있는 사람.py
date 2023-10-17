import sys
input = sys.stdin.readline
a = []
for _ in range(int(input())):
    t = input().split()
    if t[1] == 'enter':
        a.append(t[0])
    else:
        a.remove(t[0])
a.sort(reverse=True)
for i in a:
    print(i)