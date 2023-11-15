from itertools import combinations
n , m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
s = set()
for ins in combinations(arr, m):
    s.add(ins)
for i in sorted(list(s)):
    print(*i)