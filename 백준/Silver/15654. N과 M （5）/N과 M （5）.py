from itertools import permutations
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
for i in permutations(arr, m):
    print(*i)