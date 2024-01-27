v, e = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(e)]

edges.sort(key = lambda x:x[2])
parent = [i for i in range(v+1)]

def find(x):
    if parent[x] == x:
        return x
    
    return find(parent[x])

def union(a,b):
    a, b = find(a), find(b)
    if a > b:
        parent[b] = a
    else:
        parent[a] = b
    
ans = 0
cnt = 0
i = 0
while cnt < v-1:
    a, b, c = edges[i]
    if find(a) == find(b):
        i += 1
        continue

    union(a,b)
    i += 1
    cnt += 1
    ans += c
    
print(ans)