from itertools import permutations, combinations
n, k = input().split()
n = tuple(map(int, n))
l = len(n)
k = int(k)
graph = list(permutations(n))
s = {0,}
while k:
    t = set()
    for i in s:
        n = graph[i]
        for p1, p2 in combinations(range(l),2):
            temp = list(n)
            temp[p1], temp[p2] = temp[p2], temp[p1]
            if temp[0] == 0:
                continue
            temp = tuple(temp)
            t.add(graph.index(temp))
    s = t
    k -= 1
temp = []
for v in s:
    temp.append(graph[v])
print(''.join(map(str,max(temp)))) if temp else print(-1)