import sys
def find(n,k):
    l = int((2*n//k)**0.5)  # 몇번째 멀리뛰기인지
    if l**2+l <= 2*n/k:
        l += 1
    if l%2:  # 오른쪽으로 가다가 끝나면
        return k*(1-l**2)//2+n, 'R'
    else:
        return l**2*k//2-n, 'L'
    

T = int(sys.stdin.readline())
for tc in range(1,T+1):
    n, k = map(int, sys.stdin.readline().split())
    n -= 1
    print(*find(n,k))