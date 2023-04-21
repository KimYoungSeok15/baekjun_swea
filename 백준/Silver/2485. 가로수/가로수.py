import math, sys
n = int(sys.stdin.readline())
lst = [int(input()) for _ in range(n)]
temp = []
for i in range(n-1):
    temp.append(lst[i+1] - lst[i])
print((max(lst) - min(lst))//math.gcd(*temp)-n+1)