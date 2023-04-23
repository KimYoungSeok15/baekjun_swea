sero, garo, t = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(sero)]

d = ((1,0),(-1,0),(0,1),(0,-1))

for i in range(2, sero-3):  # 청소기의 위치를 저장
    if room[i][0] == -1:
        cleaner_row = (i, i+1)
        break
while t:  # 시간이 될 떄 까지
    to_be_dispersed = [[0]*garo for _ in range(sero)]  # 확산 예정 리스트    
    # 확산 예약
    for r in range(sero):
        for c in range(garo):
            if room[r][c] >= 5:
                dirt = room[r][c]//5
                cnt = 0
                for dr, dc in d:
                    if 0<=r+dr<=sero-1 and 0<=c+dc<=garo-1 and room[r+dr][c+dc] != -1:
                        to_be_dispersed[r+dr][c+dc] += dirt
                        cnt += 1
                room[r][c] -= cnt * dirt
    # 확산 적용
    for r in range(sero):
        for c in range(garo):
            munzi = to_be_dispersed[r][c]
            if munzi:
                room[r][c] += munzi
    # 공기 순환

    # 공기 청정기 위쪽(반시계)
    for i in range(cleaner_row[0]-1,0,-1):  # 첫 열
        room[i][0] = room[i-1][0]
    for i in range(0,garo-1):  # 첫 행
        room[0][i] = room[0][i+1]        
    for i in range(0,cleaner_row[0]):  # 마지막 열
        room[i][garo-1] = room[i+1][garo-1]
    for i in range(garo-1,1,-1):  # 공기청정기 위쪽 부분 행
        room[cleaner_row[0]][i] = room[cleaner_row[0]][i-1]
    room[cleaner_row[0]][1] = 0

    # 공기 청정기 아래쪽(시계)
    for i in range(cleaner_row[1]+1, sero-1):  # 첫 열
        room[i][0] = room[i+1][0]
    for i in range(garo-1):  # 마지막 행
        room[sero-1][i] = room[sero-1][i+1]        
    for i in range(sero-1,cleaner_row[1],-1):  # 마지막 열
        room[i][garo-1] = room[i-1][garo-1]
    for i in range(garo-1,1,-1):  # 공기청정기 아래쪽 부분 행
        room[cleaner_row[1]][i] = room[cleaner_row[1]][i-1]    
    room[cleaner_row[1]][1] = 0      

    t -= 1
ans = 0
for i in range(sero):
    for j in range(garo):
        ans += room[i][j]
print(ans+2)