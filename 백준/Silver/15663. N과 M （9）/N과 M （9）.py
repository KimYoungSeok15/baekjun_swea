from itertools import permutations
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ans = set()
for i in permutations(arr,m):
    ans.add(i)
ans = sorted(list(ans))
for j in ans:
    print(*j)
