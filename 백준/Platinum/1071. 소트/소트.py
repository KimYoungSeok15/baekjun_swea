n = int(input())
arr = list(map(int, input().split()))
cnt = [0] * 1001
for i in arr:
    cnt[i] += 1

num = []
for i in range(1001):
    if cnt[i]:
        num.append([i, cnt[i]])


def solve(remaining_cnt, cur_comb):
    if len(cur_comb) == n:
        print(*cur_comb)
        exit()

    for i in range(len(remaining_cnt)):
        if remaining_cnt[i][1] and (
            not cur_comb or cur_comb[-1] + 1 != remaining_cnt[i][0]
        ):
            remaining_cnt[i][1] -= 1
            cur_comb.append(remaining_cnt[i][0])
            solve(remaining_cnt, cur_comb)
            remaining_cnt[i][1] += 1
            cur_comb.pop()


solve(num, [])
