i=input
g=[i() for _ in range(int(i()))]
g.sort()
g.sort(key=lambda x:sum([int(j) if j.isnumeric() else 0 for j in x]))
g.sort(key=lambda x:len(x))
for k in g:
  print(k)