# 1-4-2-3-1

n = int(input())
lst = [list(map(int, input().split())) for _ in range(6)]
hor, ver = 0, 0
for move in lst:
    if move[0] == 1:
        hor += move[1]
    elif move[0] == 3:
        ver += move[1]
for i in range(6):
    if lst[i][0] == 1 and lst[(i+1)%6][0] != 4:
        temp = lst[i][1]*lst[(i+1)%6][1]
    elif lst[i][0] == 4 and lst[(i+1)%6][0] != 2:
        temp = lst[i][1]*lst[(i+1)%6][1]    
    elif lst[i][0] == 2 and lst[(i+1)%6][0] != 3:
        temp = lst[i][1]*lst[(i+1)%6][1]           
    elif lst[i][0] == 3 and lst[(i+1)%6][0] != 1:
        temp = lst[i][1]*lst[(i+1)%6][1]   
    else:
        continue
print(n*(hor*ver-temp))