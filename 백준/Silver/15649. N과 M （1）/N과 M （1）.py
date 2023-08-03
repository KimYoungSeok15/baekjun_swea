from itertools import permutations as p
n,m=map(int,input().split())
for i in p(range(1,n+1),m):
  print(*i)