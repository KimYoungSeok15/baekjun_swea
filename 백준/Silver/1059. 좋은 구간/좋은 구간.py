l = int(input())
lst = sorted(list(map(int, input().split())))
n = int(input())
for i in range(l):
    if lst[i] == n:
        print(0)
        exit()
    if lst[i] > n:
        break
if i == 0:
    print((n)*(lst[0]-n)-1)
    exit()
a, b = lst[i-1], lst[i]
print((n-lst[i-1])*(lst[i]-n)-1)