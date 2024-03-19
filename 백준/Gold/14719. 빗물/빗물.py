h, w = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
for i in range(w-1):
  if arr[i]:
    for j in range(1,arr[i]+1):
      now = i+1
      while now < w:
        if arr[now] < j:
          now += 1
          continue
        else:
          break
      if now == w:
        continue
      ans += now-i-1
print(ans)