t = input()
now = t[0]
ans = 0
for i in t:
  if i != now:
    ans += 1
    now = i
print((ans+1)//2)