n = int(input())
k = int(input())
lst = sorted(list(map(int, input().split())))
if k == 1:
    print(max(lst)-min(lst))
    exit()
dist = []
for i in range(n-1):
    dist.append(lst[i+1]-lst[i])
dist.sort()
print(sum(dist[:-k+1]))