import sys
input = sys.stdin.readline
r, c = map(int, input().split())
board = [input() for _ in range(r)]
d = ((1,0),(0,1),(-1,0),(0,-1))
mark = [0]*26
mark[ord(board[0][0])-65] = 1
ans = 0
def search(y,x, score):
    global ans
    ans = max(ans, score)
    for dy, dx in d:
        ny, nx = y+dy, x+dx
        if 0<=ny<r and 0<=nx<c  and not mark[ord(board[ny][nx])-65]:
            mark[ord(board[ny][nx])-65] = 1
            search(ny,nx, score+1)
            mark[ord(board[ny][nx])-65] = 0
search(0,0,1)
print(ans)