for tc in range(int(input())):
    n = int(input())
    arr = list(map(lambda x:int(x)-1, input().split()))
    v = [0]*n
    cnt = 0
    for i in range(n):
        if not v[i]:
            v[i] = 1
            cnt += 1
            now = arr[i]
            while now != i:
                v[now] = 1
                now = arr[now]
    print(cnt)
