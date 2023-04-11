n = int(input())
a = int(input())
if n == 1:
    print(0)
    exit()
lst = sorted([int(input()) for _ in range(n-1)], reverse = True)
cnt = 0
while a<=lst[0]:
    a += 1
    lst[0] -= 1
    lst.sort(reverse=True)
    cnt += 1
print(cnt)
