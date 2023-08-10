def search(row, col):  # 현재 행, 열, 현재까지 놓은 넴모, 목표 넴모
    global ans, n, m
    if col == m:
        if row == n-1:
            ans +=1
            return
        else:
            row += 1
            col = 0

    # 불가능한 경우 (여기에 놓으면 2x2가 완성된다면)
    search(row, col+1)
    if 1<=row and 1<=col and lst[row-1][col-1] and lst[row-1][col] and lst[row][col-1]:  
        return
    # 놓는 경우
    else:
        lst[row][col] = 1         
        search(row, col+1)
        lst[row][col] = 0
       
n, m = map(int, input().split())  # 입력
if n == 1:
    print(2**m)
    exit()
if m == 1:
    print(2**n)
    exit()
ans = 0
lst = [[0]*m for _ in range(n)]
search(0, 0)
print(ans)
            
        