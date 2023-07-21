import sys
i = sys.stdin.readline
t=[i()[:-1] for _ in range(int(i()))]
m=[]
t.sort()
t.sort(key=lambda x:len(x))
for i in t:
    if i not in m:
        print(i)
        m.append(i)


