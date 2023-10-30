from collections import deque
n = int(input())
q = deque(list(range(1,n+1)))
while True:
    print(q.popleft(), end=' ')
    if q:
        q.append(q.popleft())
    else:
        break