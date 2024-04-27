from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))
oper = list(map(int, input().split()))
lst = ["+"] * oper[0] + ["-"] * oper[1] + ["*"] * oper[2] + ["/"] * oper[3]
max_ans, min_ans = -int(1e9), int(1e9)
for comb in permutations(lst):
    ans = arr[0]
    for i in range(n - 1):
        if comb[i] == "+":
            ans += arr[i + 1]
        elif comb[i] == "-":
            ans -= arr[i + 1]
        elif comb[i] == "*":
            ans *= arr[i + 1]
        else:
            ans = int(ans / arr[i + 1])
    max_ans = max(max_ans, ans)
    min_ans = min(min_ans, ans)
print(max_ans)
print(min_ans)
