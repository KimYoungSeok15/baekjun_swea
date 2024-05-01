from itertools import combinations
from bisect import bisect

N = int(input())
arr = sorted([*map(int, input().split())])
ans = int(4e9)
for comb in combinations(range(N), 2):
    n1, n2 = comb
    temp_sum = sum((arr[n1], arr[n2]))
    idx = bisect(arr, -temp_sum)
    if 0 < idx <= N - 1:
        left = idx - 1
        right = idx
        while left in comb:
            left -= 1
        while right in comb:
            right += 1

        if left < 0:
            t_idx = right
        elif right > N - 1:
            t_idx = left
        else:
            if abs(temp_sum + arr[left]) > abs(temp_sum + arr[right]):
                t_idx = right
            else:
                t_idx = left

    elif idx == N:
        if n2 == N - 1:
            continue
        else:
            t_idx = N - 1

    else:
        if n1 == 0:
            continue
        else:
            t_idx = 0

    temp_sum += arr[t_idx]
    if ans > abs(temp_sum):
        ans = abs(temp_sum)
        ans_set = (arr[n1], arr[n2], arr[t_idx])

print(*sorted(ans_set))
