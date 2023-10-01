n, s = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
for i in range(1<<n):
    t = []
    for j in range(n):
        if i & 1<<j:
            t.append(arr[j])
    if t and sum(t) == s:
        ans += 1

print(ans)