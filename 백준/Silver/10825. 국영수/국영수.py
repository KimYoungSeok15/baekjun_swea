import sys
input = sys.stdin.readline
arr = [input().split() for _ in range(int(input()))]
arr.sort()
arr.sort(key=lambda x:int(x[3]), reverse=True)
arr.sort(key=lambda x:int(x[2]))
arr.sort(key=lambda x:int(x[1]), reverse=True)
for i in arr:
  print(i[0])