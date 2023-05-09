from collections import deque

n = int(input())
lst = list(map(int, input().split()))
d = int(input())

ans = 0

for i in range(n):
    if lst[i] == -1:
        root = i
        break
 
if root == d:
    print(0)
    exit()    
    
q = deque([root])

while q:
    now = q.popleft()
    is_leaf = True
    for i in range(n):
        if lst[i] == now and i != d:
            q.append(i)
            is_leaf = False
    if is_leaf:
        ans += 1

print(ans)