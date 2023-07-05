n = int(input())
arr = [input() for _ in range(n)]
temp = arr[0]
l = len(temp)
pattern = [0]*l
for i in range(1,n):
    for j in range(l):
        if temp[j] != arr[i][j]:
            pattern[j] = 1
for i in range(l):
    if pattern[i]:
        print('?', end='')
    else:
        print(temp[i], end='')