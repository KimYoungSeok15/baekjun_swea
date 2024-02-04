from collections import deque
n = int(input())
parent = list(map(int, input().split()))
d = int(input())
for idx, val in enumerate(parent):
    if val == -1:
        root = idx
        break

leaf_possible = [1]*n
for i in range(n):
    if i != root:
        leaf_possible[parent[i]] = 0
if n == 1:
    leaf_possible[0] = 1
if parent.count(parent[d]) == 1:
    leaf_possible[parent[d]] = 1

def is_root(now):
    if now == d:
        return False
    while True:
        if parent[now] == d:
            return False
        elif parent[now] == root:
            return True
        else:
            now = parent[now]

ans = 0
for idx in range(n):
    if leaf_possible[idx]:
        if is_root(idx):
            ans += 1
            
print(ans)
    
