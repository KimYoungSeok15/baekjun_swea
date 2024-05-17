k = int(input())

if k == 1:
    print(0)
    exit()

cnt = 0
while 1:
    s = 1

    #  2**(s-1) < k <= 2**s이 되도록
    while 2**s < k:
        s += 1

    k -= 2 ** (s - 1)
    cnt += 1

    if k == 1:
        break

print(cnt % 2)
