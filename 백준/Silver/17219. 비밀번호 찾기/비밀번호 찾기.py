i=input
n,m=map(int,i().split())
d=dict()
for _ in range(n):
  t=i().split()
  d[t[0]]=t[1]
for _ in range(m):
  print(d[i()])