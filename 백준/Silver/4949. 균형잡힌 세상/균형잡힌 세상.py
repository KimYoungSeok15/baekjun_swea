import sys
input = sys.stdin.readline
while True:
  temp = input().rstrip()
  if temp == '.':
    break
  s = []
  for i in temp:
    if i == '[':
      s.append('[')
    elif i == '(':
      s.append('(')
    elif i == ']':
      if not s:
        print('no')
        break
      t = s.pop()
      if t != '[':
        print('no')
        break
    elif i == ')':
      if not s:
        print('no')
        break
      t = s.pop()
      if t != '(':
        print('no')
        break
  else:
    if not s:
      print('yes')
    else:
      print('no')