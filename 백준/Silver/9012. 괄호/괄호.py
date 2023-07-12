from sys import stdin
from collections import deque
input = stdin.readline
for tc in range(int(input())):
    blank = deque(list(input()))
    blank.pop()
    s = []
    flag = True
    while blank:
        put = blank.popleft()
        if put == '(':
            s.append('(')
        else:
            if not s:
                print('NO')
                flag = False
                break
            elif s[-1] == '(':
                s.pop()
            else:
                s.append(')')
    if flag and s:
        print('NO')
        continue
    elif flag:
        print('YES')