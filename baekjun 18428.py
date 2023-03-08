n = int(input())
lst = [input().split() for _ in range(n)]
T = []
S = []
X = []
for i in range(n):
    for j in range(n):
        if lst[i][j] == 'T':
            T.append([i, j])
        elif lst[i][j] == 'S':
            S.append([i, j])
        else:
            X.append([i, j])
search_lst = []
# 각 학생에 대해 가로 세로에 있는 X들을 찾아 검색 대상으로 선정
for s in S:

    r, c = s[0], s[1]
    while r < n-1 and lst[r+1][c] == 'X':
        if not [r+1, c] in search_lst:
            search_lst.append([r+1 , c])
        r += 1

    r, c = s[0], s[1]
    while r > 0 and lst[r-1][c] == 'X':
        if not [r-1, c] in search_lst:        
            search_lst.append([r-1 , c])
        r -= 1     

    r, c = s[0], s[1]
    while c < n-1 and lst[r][c+1] == 'X':
        if not [r, c+1] in search_lst:        
            search_lst.append([r , c+1])
        c += 1   
        
    r, c = s[0], s[1]
    while c > 0 and lst[r][c-1] == 'X':
        if not [r, c-1] in search_lst:        
            search_lst.append([r , c-1])
        c -= 1

# 방해물을 놓을 수 있는 곳들에 대해 방해물 3개를 놓을 수 있는 모든 경우의 수
obs = []
for i in range(1<<len(search_lst)):
    temp = []
    for j in range(len(search_lst)):
        if i & 1<<j:
            temp.append(j)
    if len(temp) == 3:
        obs.append([search_lst[idx] for idx in temp])
        
origin_map = [i[:] for i in lst]  # 기존 맵 저장
for trial in obs:  # 모든 방해물을 놓는 경우의 수에 대해
    lst = [i[:] for i in origin_map]  # 맵 초기화
    for i in range(3):  # 방해물을 놓는다.
        row, col = trial[i][0], trial[i][1]
        lst[row][col] = 'O'

    for s in S:  # 각 학생들에 대해 감시를 피하는지 검사
        caught = False       

        r, c = s[0], s[1]
        while r < n-1:  # 아래쪽 조사
            if lst[r+1][c] == 'T':
                caught = True
                break
            elif lst[r+1][c] == 'X':         
                r += 1
                continue
            else:
                break
        if caught:
            break

        r, c = s[0], s[1]
        while r > 0:  # 위쪽 조사
            if lst[r-1][c] == 'T':
                caught = True
                break
            elif lst[r-1][c] == 'X':         
                r -= 1
                continue
            else:
                break
        if caught:
            break

        r, c = s[0], s[1]
        while c < n-1:  # 오른쪽 조사
            if lst[r][c+1] == 'T':
                caught = True
                break
            elif lst[r][c+1] == 'X':         
                c += 1
                continue
            else:
                break
        if caught:
            break  
            
        r, c = s[0], s[1]
        while c > 0:  # 왼쪽 조사
            if lst[r][c-1] == 'T':
                caught = True
                break
            elif lst[r-1][c-1] == 'X':         
                c -= 1
                continue
            else:
                break
        if caught:
            break
    else:  # 모든 감시를 피했다면
        print('YES')
        break
else:
    print('NO')
