n = int(input())
com = [input().split() for _ in range(n)]
undo = []
ans = ''
for i in range(n-1, -1, -1):
    if com[i][0] == 'undo':
        for u in undo:
            if u[0] <= int(com[i][2]) <= u[1]:
                break
        else:
            start, end = int(com[i][2])-int(com[i][1]), int(com[i][2])
            undo.append([start,end])
for j in range(n):
    for u in undo:
        if u[0] <= int(com[j][2]) <= u[1]:
            break
    else:
        ans = ans + com[j][1]
print(ans)