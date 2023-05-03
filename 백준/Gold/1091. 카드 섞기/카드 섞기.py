n = int(input())
p = list(map(int, input().split()))
s = list(map(int, input().split()))
ans = [0,1,2]*(n//3)
org = p[:]
cnt = 0
check_list = [i for i in range(n)]
while True:
    if p==ans:
        print(cnt)
        exit()   
    temp = [0]*n       
    for idx, value in enumerate(s):
        temp[value] = p[idx]
    p = temp[:]
    cnt += 1
    if p == org:
        print(-1)
        exit()    