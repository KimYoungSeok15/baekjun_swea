from itertools import permutations
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = int(1e9)
for case in permutations(range(n)):
    temp = 0
    for i in range(n-1):
        if not arr[case[i]][case[i+1]]:
            break
        temp += arr[case[i]][case[i+1]]
    else:
        if not arr[case[n-1]][case[0]]:
            continue
        temp += arr[case[n-1]][case[0]]
        ans = min(ans, temp)
print(ans)