n, k = map(int, input().split())
lst = list(map(int,input().split()))
best = sum(lst[:k])
temp = sum(lst[:k])
for i in range(n-k):
    temp += lst[i+k] - lst[i]
    best = max(best, temp)
print(best)