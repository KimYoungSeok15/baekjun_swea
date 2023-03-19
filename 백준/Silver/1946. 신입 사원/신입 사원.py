T = int(input())
for tc in range(T):
    n = int(input())
    apply= sorted([list(map(int,input().split())) for _ in range(n)])
    limit = apply[0][1]
    cnt = 1
    i = 1
    if n == 1:
        print(1)
        continue
    if limit == 1:
        print(1)
        continue        
    while True:
        if apply[i][1] < limit:
            cnt += 1
            limit = apply[i][1]
            if limit == 1:
                break        
        i += 1
    print(cnt)