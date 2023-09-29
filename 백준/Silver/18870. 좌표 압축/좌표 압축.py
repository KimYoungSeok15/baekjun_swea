n = int(input())
arr = list(map(int, input().split()))
arr2 = sorted(arr)
d = dict()
cnt = 0
for i in range(len(arr)):
    try:
        d[arr2[i]]
    except:
        d[arr2[i]] = cnt
        cnt += 1
for j in arr:
    print(d[j], end=' ')
print()