import sys
input = sys.stdin.readline
u, n = map(int, input().split())
call = [list(map(lambda x:int(x) if x.isdigit() else x, input().split())) for _ in range(n)]
memo = [0]*(u+1)

for c in call:
    memo[c[1]] += 1
    
least = 10001

for i in range(u+1):
    if memo[i] and memo[i] < least:
        least = memo[i]
        index = [i]
    elif memo[i] and memo[i] == least:
        index.append(i)

if len(index) == 1:
    for i in range(n):
        if call[i][1] == index[0]:
            print(*call[i])
            exit()
else:
    for i in range(u+1):
        if memo[i] == least:
            price = i
            break
    for j in range(n):
        if call[j][1] == price:
            print(*call[j])
            break