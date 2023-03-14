import sys
sys.setrecursionlimit(1000000)
r, c = map(int, input().split())
field = [input() for _ in range(r)]
wolves = []
sheeps = []
visited = [[0]*c for _ in range(r)]
v_cnt = 0
o_cnt = 0
def dfs(row, col, v, o):
    visited[row][col] = 1
    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
        if r-1>=row+dr>=0 and c-1>=col+dc>=0 and not visited[row+dr][col+dc] and field[row+dr][col+dc] != '#':
            v, o = dfs(row+dr, col+dc, v, o)
    if field[row][col] == 'v':
        v += 1
    elif field[row][col] == 'o':
        o += 1            
    return v, o
#  모든 점에 대해 
for i in range(r):
    for j in range(c):
        if not visited[i][j] and field[i][j] != '#':  # 울타리가 아닌 비방문 지역이면
            wolf, sheep = dfs(i,j,0,0)
            if wolf < sheep :
                o_cnt += sheep
            else:
                v_cnt += wolf
print(o_cnt, v_cnt)