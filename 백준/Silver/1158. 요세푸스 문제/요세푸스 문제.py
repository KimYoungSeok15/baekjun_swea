n, k = map(int, input().split())
q = list(range(1,1+n))
idx = -1
ans = []
while q:
    t = k
    if idx + t >= len(q):
        while t:
            if idx + t >= len(q):
                t -= len(q)-idx
                idx = 0
            else:
                idx += t
                t = 0
    else:
        idx += k
    ans.append(q.pop(idx))
    idx -= 1
    if idx == len(q):
        idx = 0
    
print('<'+str(ans)[1:-1]+'>')