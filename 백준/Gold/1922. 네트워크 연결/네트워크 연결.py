import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
edge = [list(map(int, input().split())) for _ in range(m)]

edge.sort(key = lambda x:x[2])
root = [i for i in range(n+1)]
ans = 0

def find(x):
    if root[x] == x:
        return x
    
    return find(root[x])

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        root[b] = a
    else:
        root[a] = b
    
i = cnt = 0
while cnt < n-1:
    a, b, c = edge[i]
    
    if find(a) == find(b):
        i += 1
        continue
    
    union(a,b)
    ans += c
    cnt += 1
    i += 1
print(ans)