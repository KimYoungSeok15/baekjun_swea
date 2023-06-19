from itertools import combinations
l, c = map(int, input().split())
arr = sorted(list(input().split()))
vowel = ['a','e','i','o','u']
ans = []
for comb in combinations(arr, l):
    score1 = score2 = 0
    for char in comb:
        if char in vowel:
            score1 += 1
        else:
            score2 += 1
    if score1 == 0 or score2 <= 1:
        continue
    ans.append(comb)
for lst in ans:
    for alphabet in lst:
        print(alphabet, end='')
    print()