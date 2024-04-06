n = int(input())
arr = list(map(int, input().split()))
s = []
for i, val in enumerate(arr):
    while s and s[-1][1] < val:
        s.pop()
    if not s:
        print(0, end=" ")
        s.append((i + 1, val))
    else:
        print(s[-1][0], end=" ")
        s.append((i + 1, val))
