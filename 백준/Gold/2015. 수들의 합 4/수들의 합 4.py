N, K = map(int, input().split())
arr = list(map(int, input().split()))
d = {0: 1}
s = 0
ans = 0
for i in range(N):
    s += arr[i]
    try:
        ans += d[s-K]
    except:
        pass
    
    try:
        d[s] += 1
    except:
        d[s] = 1


print(ans)
