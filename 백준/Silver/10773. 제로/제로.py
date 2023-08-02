i,t,s=input,int,[]
for _ in range(t(i())):
 q=t(i())
 s.append(q) if q else s.pop()
print(sum(s))