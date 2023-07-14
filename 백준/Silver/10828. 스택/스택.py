import sys
input = sys.stdin.readline
n = int(input())
s = []
for _ in range(n):
    command = input().split()
    if len(command)>1:
        s.append(int(command[1]))
    elif command[0] == 'pop':
        if s:
            print(s.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(s))
    elif command[0] == 'empty':
        if s:
            print(0)
        else:
            print(1)
    else:
        if s:
            print(s[-1])
        else:
            print(-1)
        