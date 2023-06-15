from itertools import permutations
n = int(input())
arr = list(map(int, input().split()))
best_ans = 0
for inst in permutations(arr):
    ans = 0
    lst = list(range(len(inst)))    
    for i in range(len(inst)):
        if inst[i] == 50:
            print(1)
            exit()
        asc = lst[i+1:]+lst[:i]
        des = list(reversed(asc))
        sum_asc, sum_des = inst[i], inst[i]
        for j in asc:
            sum_asc += inst[j]
            if sum_asc > 50:
                break
            elif sum_asc == 50:
                ans += 1
                break
        for k in des:
            sum_des += inst[k]
            if sum_des > 50:
                break
            elif sum_des == 50:
                ans += 1
                break
    best_ans = max(best_ans, ans)
print(best_ans//4)

