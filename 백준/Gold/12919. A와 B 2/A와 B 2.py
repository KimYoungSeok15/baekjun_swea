from collections import deque

s = input()
q = deque([[s, len(s)]])
t = input()
reversed_t = t[::-1]
tl = len(t)


while q:
    now, l = q.popleft()
    rev = "B" + now[::-1]

    # 종료조건
    if l == tl and t == now:
        print(1)
        exit()

    # 정방향이든 역방향이든 포함한다면
    if t.find(now) != -1 or reversed_t.find(now) != -1:
        q.append([now + "A", l + 1])
        q.append([rev, l + 1])

print(0)
