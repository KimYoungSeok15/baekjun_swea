move = []
visited = [[0]*6 for _ in range(6)]
for _ in range(36):
    temp = input()
    move.append((ord(temp[0])-ord('A'),int(temp[1])-1))
move.append((move[0][0],move[0][1]))
        
for i in range(36):
    if (abs(move[i][0]-move[i+1][0]), abs(move[i][1]-move[i+1][1])) in ((2,1),(1,2)) and not visited[move[i][0]][move[i][1]]:
        visited[move[i][0]][move[i][1]] = 1
    else:
        print('Invalid')
        exit()
print('Valid')
        