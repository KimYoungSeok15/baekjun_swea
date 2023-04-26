n = int(input())
input = list(map(int, input().split()))
used = [False]*n
ans = [0]*n
def perm(k):
    if k == n:
        if check():
            print(*ans)
        return
    for i in range(n):
        if not used[i]:        
            ans[k] = i+1
            used[i] = True
            perm(k+1)
            used[i] = False
            
def check():
    for i in range(n):
        cnt = 0
        height = input[ans[i]-1]
        for j in range(i):
            if ans[j]-1 > ans[i]-1:
                cnt += 1
        if cnt != height:
            return False
    return True

perm(0)    