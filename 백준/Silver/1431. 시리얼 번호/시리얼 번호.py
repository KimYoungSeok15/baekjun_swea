i=input
g=[i() for _ in range(int(i()))]
g.sort(key=lambda x:(len(x),sum([int(j) if j.isnumeric() else 0 for j in x]),x))
for k in g:
  print(k)