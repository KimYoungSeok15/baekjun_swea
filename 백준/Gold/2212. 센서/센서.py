n = int(input())
k = int(input())
lst = sorted(list(map(int, input().split())))
dist = []
for i in range(n-1):
    dist.append(lst[i+1]-lst[i])

while k > 1 and dist:
    dist.remove(max(dist))
    k -= 1
print(sum(dist))