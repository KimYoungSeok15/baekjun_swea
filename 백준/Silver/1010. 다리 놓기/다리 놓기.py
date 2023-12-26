from math import comb
for _ in range(int(input())):
    a, b = map(int, input().split())
    print(comb(max(a,b), min(a,b)))