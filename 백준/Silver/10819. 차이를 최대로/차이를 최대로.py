from itertools import permutations
n = int(input())
arr = list(map(int, input().split()))
ans = 0
for case in permutations(arr):
  temp = 0
  for i in range(n-1):
    temp += abs(case[i]-case[i+1])
  ans = max(ans, temp)
print(ans)
    