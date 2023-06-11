import sys
input = sys.stdin.readline
n = int(input())
stdnt = [list(map(int, input().split())) for _ in range(n**2)]
board = [[0]*n for _ in range(n)]
d = ((1,0),(0,1),(-1,0),(0,-1))
for s in range(n**2):
    num, likes = stdnt[s][0], stdnt[s][1:]  # 4 [2, 5, 1, 7]
    score = [[[-1,-1] for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if not board[r][c]:
                score[r][c] = [0,0]
                for dr, dc in d:
                    if 0<=r+dr<n and 0<=c+dc<n:
                        if board[r+dr][c+dc] in likes:
                            score[r][c][0] += 1
                        elif not board[r+dr][c+dc]:
                            score[r][c][1] += 1
    top_score = -1
    for i in range(n):
        for j in range(n):
            now = score[i][j][0]
            if now >= 0:
                if now > top_score:
                    top_score = now
                    top_place = [(i,j,score[i][j][1])]
                elif now == top_score:
                    top_place.append((i,j,score[i][j][1]))
    if len(top_place) > 1:
        top_place.sort(reverse=True, key=lambda x:x[-1])
        if top_place[0][-1] == top_place[1][-1]:
            cand = []
            for t in top_place:
                if t[-1] == top_place[0][-1]:
                    cand.append(t)
            cand.sort()
            board[cand[0][0]][cand[0][1]] = num
            continue
    board[top_place[0][0]][top_place[0][1]] = num
    
ans = 0
dic = {4:1000, 3:100, 2:10, 1:1, 0:0}
for r in range(n):
    for c in range(n):
        now = board[r][c]
        for k in range(n**2):
            if stdnt[k][0] == now:
                cnt = 0
                for dr, dc in d:
                    if 0<=r+dr<n and 0<=c+dc<n and board[r+dr][c+dc] in stdnt[k][1:]:
                        cnt += 1
                ans += dic[cnt]
print(ans)