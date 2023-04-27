n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
cut = [lst[:]]
blue, white = 0, 0
while cut:
    temp = []    
    for sqr in cut:
        l = len(sqr) 
        col = sqr[0][0]
        flag = True
        for r in range(l):
            if not flag:
                break
            for c in range(l):
                if sqr[r][c] != col:
                    for j in range(2):
                        for k in range(2):
                            temp.append([sqr[j*l//2+i][k*l//2:k*l//2 + l//2] for i in range(l//2)])
                    flag = False
                    break
        if flag:
            if col == 1:
                blue += 1
            else:
                white += 1
    if temp:
        cut = temp[:]
    else:
        break
print(white)
print(blue)