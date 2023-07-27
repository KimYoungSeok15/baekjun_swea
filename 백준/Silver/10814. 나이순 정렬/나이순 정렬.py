import sys
input = sys.stdin.readline
n = int(input())
arr = [[] for _ in range(201)]
for i in range(n):
    temp = input().split()
    arr[int(temp[0])].append(temp[1])
for i in range(201):
    for item in arr[i]:
        print(i, item)

