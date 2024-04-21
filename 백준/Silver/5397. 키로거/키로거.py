from collections import deque

for tc in range(int(input())):
    s = input()
    d1, d2 = deque(), deque()
    for i in s:
        if i == "<":
            if d1:
                d2.appendleft(d1.pop())
        elif i == ">":
            if d2:
                d1.append(d2.popleft())
        elif i == "-":
            if d1:
                d1.pop()
        else:
            d1.append(i)
    print("".join(d1) + "".join(d2))
