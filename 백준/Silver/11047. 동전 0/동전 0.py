n, k = map(int, input().split())
coin = list(reversed([int(input()) for _ in range(n)]))
i = 0
ans = 0
while i < n:
    if coin[i] <= k:
       k -= coin[i]
       ans += 1
    else:
        i += 1
print(ans) 
