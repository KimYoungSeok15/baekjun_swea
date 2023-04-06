n, a, b = map(int,input().split())
a, b = min(a,b), max(a,b)
cnt = 1
while not a % 2 or not b - a == 1:
    n = (n+1)//2
    a = (a+1)//2
    b = (b+1)//2
    cnt += 1
print(cnt)