n, l = map(int, input().split())
leak_lst = sorted(list(map(int, input().split())))
temp = []
cnt = 0
for i in range(n):
    if temp and temp[0] + l > leak_lst[i]:
        temp.append(leak_lst[i])
    else:
        if temp:
            cnt += 1
        temp = [leak_lst[i]]
print(cnt+1)
