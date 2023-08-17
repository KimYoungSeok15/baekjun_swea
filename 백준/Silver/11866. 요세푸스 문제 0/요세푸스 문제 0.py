n, k =map(int, input().split())
q = list(range(1,n+1))
ans = []
now = k-1
while q:
  ans.append(q.pop(now))
  now += k-1
  if not q:
    print('<'+str(ans)[1:-1]+'>')
    exit()
  while now >= len(q):
    now -= len(q)