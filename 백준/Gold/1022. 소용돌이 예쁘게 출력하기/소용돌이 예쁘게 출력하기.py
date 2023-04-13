# n번째 껍질의 가장 큰 수 : n-1,n-1에 위치, 값 = 1+4n(n-1) = 4n^2-4n+1
# n번째 껍질의 수 범위 : 4n^2-12n+10~4n^2-4n+1
r1, c1, r2, c2 = map(int, input().split())
if abs(r1)-abs(c1) == 0:
    shell1 = abs(r1)+1
else:
    if abs(r1) > abs(c1):
        shell1 = abs(r1)+1
    else:
        shell1 = abs(c1)+1

if abs(r2)-abs(c2) == 0:
    shell2 = abs(r2)+1
else:
    if abs(r2) > abs(c2):
        shell2 = abs(r2)+1
    else:
        shell2 = abs(c2)+1
shell = max(shell1, shell2)
lst = [[0]*(c2-c1+1) for _ in range(r2-r1+1)]
if shell == 1:
    print(1)
    exit()
cnt = 2
if c1<=0<=c2 and r1<=0<=r2:  
    lst[-r1][-c1] = 1
for i in range(1,shell):
    r, c = i-1, i
    if c1<=c<=c2 and r1<=r<=r2:    
        lst[r-r1][c-c1] = cnt
    while not abs(r) == abs(c):
        r-=1
        cnt += 1
        if c1<=c<=c2 and r1<=r<=r2:    
            lst[r-r1][c-c1] = cnt
    c-=1
    cnt += 1
    if c1<=c<=c2 and r1<=r<=r2:    
        lst[r-r1][c-c1] = cnt   
    while not abs(r) == abs(c):
        c-=1
        cnt += 1
        if c1<=c<=c2 and r1<=r<=r2:    
            lst[r-r1][c-c1] = cnt
    r+=1
    cnt += 1
    if c1<=c<=c2 and r1<=r<=r2:    
        lst[r-r1][c-c1] = cnt     
    while not abs(r) == abs(c):
        r+=1
        cnt += 1
        if c1<=c<=c2 and r1<=r<=r2:    
            lst[r-r1][c-c1] = cnt
    c+=1
    cnt += 1
    if c1<=c<=c2 and r1<=r<=r2:    
        lst[r-r1][c-c1] = cnt           
    while not abs(r) == abs(c):
        c+=1
        cnt += 1
        if c1<=c<=c2 and r1<=r<=r2:    
            lst[r-r1][c-c1] = cnt    
    cnt += 1        
max_len = len(str(max(lst[0][0],lst[0][-1],lst[-1][0],lst[-1][-1])))
for row in range(r2-r1+1):
    for col in range(c2-c1+1):
        print(' '*(max_len - len(str(lst[row][col])))+str(lst[row][col]), end=' ')
    print()
    