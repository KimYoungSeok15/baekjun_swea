a = input()
ans = []
for i in range(len(a)):
  ans.append(a[i:])
ans.sort()
for i in ans:
  print(i)