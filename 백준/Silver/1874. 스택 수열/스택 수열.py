from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
arr = deque(list(range(1,n+1)))
s = []
ans = []
now = 0
for _ in range(n):
  num = int(input())
  if num > now:
    temp = 0
    cnt = 0
    t = []
    while temp != num:
      temp = arr.popleft()
      t.append(temp)
      cnt += 1
    ans.extend('+'*(cnt))
    ans.append('-')
    s.extend(t)
    s.pop()
    now = s[-1] if s else 0
  elif num == now:
    ans.append('-')
    s.pop()
    now = s[-1] if s else 0
  else:
    print('NO')
    exit()
for i in ans:
  print(i)