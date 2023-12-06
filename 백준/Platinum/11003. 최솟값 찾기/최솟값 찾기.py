import sys
from collections import deque
input=sys.stdin.readline

def solve():
    n,m=map(int, input().split())
    l=list(map(int, input().split()))
    
    que=deque([])
    ans=[0 for _ in range(n)]
    for i in range(n):
        while que and que[-1][0]>=l[i]:
            que.pop()
        que.append((l[i],i))
        if que[0][1]<(i-m+1):
            que.popleft()
        ans[i]=que[0][0]
    print(*ans)

if __name__=='__main__':
    solve()