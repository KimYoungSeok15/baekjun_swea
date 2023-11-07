from itertools import combinations_with_replacement
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ans = []
for case in combinations_with_replacement(arr, m):
    if case not in ans:
        ans.append(case)
for i in ans:
    print(*i)