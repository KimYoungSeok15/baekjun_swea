n = int(input())
lst = sorted([list(map(int, input().split())) for _ in range(n)])
[print(*i) for i in lst]