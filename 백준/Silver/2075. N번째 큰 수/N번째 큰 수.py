n = int(input())
best = list(map(int,input().split()))
for _ in range(n-1):
    lst = list(map(int,input().split()))
    best.extend(lst)
    best.sort()
    best = best[-n:]
print(best[0])