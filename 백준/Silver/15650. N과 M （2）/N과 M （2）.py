from itertools import combinations
n, m = map(int, input().split())
for p in combinations(list(range(1,n+1)), m):
    print(*p)