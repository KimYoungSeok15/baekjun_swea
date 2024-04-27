N = int(input())
nums = list(map(int, input().split()))
oper = list(map(int, input().split()))

max_ans, min_ans = -int(1e9), int(1e9)


def dfs(depth, max_now, min_now):
    global max_ans, min_ans

    if depth == N:
        max_ans = max(max_ans, max_now)
        min_ans = min(min_ans, min_now)
        return

    if oper[0]:
        oper[0] -= 1
        dfs(depth + 1, max_now + nums[depth], min_now + nums[depth])
        oper[0] += 1

    if oper[1]:
        oper[1] -= 1
        dfs(depth + 1, max_now - nums[depth], min_now - nums[depth])
        oper[1] += 1

    if oper[2]:
        oper[2] -= 1
        dfs(depth + 1, max_now * nums[depth], min_now * nums[depth])
        oper[2] += 1

    if oper[3]:
        oper[3] -= 1
        dfs(depth + 1, int(max_now / nums[depth]), int(min_now / nums[depth]))
        oper[3] += 1


dfs(1, nums[0], nums[0])

print(max_ans)
print(min_ans)
