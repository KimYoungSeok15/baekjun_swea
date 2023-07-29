import sys
from collections import deque
input = sys.stdin.readline
q = deque([])
for i in range(int(input())):
    temp = input().split()
    if temp[-1].isdigit():
        q.append(temp[-1])
    elif temp[0] == 'pop':
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif temp[0] == 'size':
        print(len(q))
    elif temp[0] == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    elif temp[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif q:
        print(q[-1])
    else:
        print(-1)