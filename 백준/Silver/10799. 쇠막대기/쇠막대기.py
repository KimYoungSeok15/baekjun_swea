a=input()
cnt = 0
ans = 0
i = 0
while i <len(a)-1:
  if a[i] == '(' and a[i+1] == '(':
    cnt += 1
    ans += 1
    i += 1
  elif a[i] == '(' and a[i+1] == ')':
    ans += cnt
    i += 2
  elif a[i] == ')':
    cnt -= 1
    i += 1
print(ans)
    
