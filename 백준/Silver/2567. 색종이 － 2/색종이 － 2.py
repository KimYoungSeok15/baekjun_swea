paper= []
for _ in range(int(input())):
    paper.append(list(map(int, input().split())))
board = [[0]*100 for _ in range(100)]
for p in paper:
    for col in range(10):
        board[p[0]+col][p[1]:p[1]+10] = [1]*10

ans = 0
for i in range(100):
    j = 0
    while j < 100:
        if board[i][j]:
            ans += 2
            cnt = 0
            while j+cnt < 100 and board[i][j+cnt]:
                cnt += 1
            if j+cnt == 100:
                break
            j += cnt
            continue
        j += 1
for i in range(100):
    j = 0
    while j < 100:
        if board[j][i]:
            ans += 2
            cnt = 0
            while j+cnt < 100 and board[j+cnt][i]:
                cnt += 1
            if j+cnt == 100:
                break
            j += cnt
            continue
        j += 1
        
print(ans)