from itertools import combinations
n, k = map(int, input().split())
k -= 5
if k<0:
    print(0)
    exit()
word = [set(input())-{'a','c','i','n','t',} for _ in range(n)]
s = set()

for w in word:
    s.update(w)

if k>=len(s):
    print(n)
    exit()
 
ans = 0
for case in combinations(s,k):
    temp = 0
    for i in range(n):
        if temp+n-i <= ans:
            break
        if word[i].issubset(case):
            temp += 1
    ans = max(ans, temp)

print(ans)
