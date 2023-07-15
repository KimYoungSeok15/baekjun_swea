n = int(input())
board = []
ans = 0
def check(r,c):
    flag = True
    for i, j in enumerate(board):
        if i-j == r-c or j == c or i+j == r+c:
            flag = False
            break
    return flag


i = j = 0
while i < n:
    while j < n:
        
        if check(i,j):
            board.append(j)
            if i == n-1:
                ans += 1
                board.pop()
                j += 1
                continue
            i += 1
            j = 0
            
        else:
            j += 1
            
    i -= 1
    if i < 0:
        print(ans)
        exit()
    j = board.pop() + 1