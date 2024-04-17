n = int(input())
inf = int(1e9)
ans = inf
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, 1 << n):
    temp_sum, temp_mul = 0, 1
    for j in range(n):
        if i & 1 << j:
            temp_sum += arr[j][1]
            temp_mul *= arr[j][0]

    ans = min(ans, abs(temp_sum - temp_mul))

print(ans)
