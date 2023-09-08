from itertools import *
n, m = map(int, input().split())
for i in combinations_with_replacement(range(1,1+n),m):
  print(*i)