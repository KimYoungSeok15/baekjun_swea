from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
arr = [input() for _ in range(n)]
q = deque([])
for i in range(n):
  new = arr[i].split()
  if len(new)> 1:
    if new[0][-1] == 'k':
      q.append(new[1])
    else:
      q.appendleft(new[1])
  elif new == ['pop_front']:
    try:
      print(q.popleft())
    except:
      print(-1)
  elif new == ['pop_back']:
    try:
      print(q.pop())
    except:
      print(-1)
  elif new == ['size']:
    print(len(q))
  elif new == ['empty']:
    print(1 if not q else 0)
  elif new == ['front']:
    try:
      print(q[0])
    except:
      print(-1)
  else:
    try:
      print(q[-1])
    except:
      print(-1)