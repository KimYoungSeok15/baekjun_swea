import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()
arr.sort(key=lambda x:x[1])
for i in arr:
    print(*i)