n, k = map(int, input().split())
arr = [0] * (n + 1)
cnt = 0
i = 2
for i in range(2, n + 1):
    if not arr[i]:
        for j in range(i, n + 1, i):
            if not arr[j]:
                arr[j] = 1
                cnt += 1
                if cnt == k:
                    print(j)
                    exit()
