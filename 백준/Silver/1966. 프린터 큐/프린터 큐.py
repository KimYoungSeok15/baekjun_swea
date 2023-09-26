for _ in range(int(input())):
  ans = 0
  n, idx = map(int, input().split())
  q = list(map(int, input().split()))
  while q:
    if q[0] == max(q):
      ans += 1
      if idx == 0:
        print(ans)
        break
      q.pop(0)
      idx -= 1
    else:
      q.append(q.pop(0))
      if idx:
        idx -= 1
      else:
        idx = len(q)-1
