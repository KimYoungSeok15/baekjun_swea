n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
d = ((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,-1),(-1,1))
ans = 0
cnt = 0
def dfs(r,c, val):
    global ans, cnt
    for dr, dc in d:
        if 0<=r+dr<n and 0<=c+dc<m and not visited[r+dr][c+dc]:
            if val == arr[r+dr][c+dc] == arr[r][c]:  # 봉우리라면
                visited[r+dr][c+dc] = True
                cnt += 1
                dfs(r+dr, c+dc, val)
            elif arr[r][c] >= arr[r+dr][c+dc]:  # 봉우리가 아니고 오르막이 아니라면
                cnt += 1
                visited[r+dr][c+dc] = True
                dfs(r+dr, c+dc, val)
while cnt < n*m:
    high = -1  
    pos = []           
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                if arr[i][j] > high:
                    high = arr[i][j]
                    pos = [(i,j)]
                elif arr[i][j] == high:
                    pos.append((i,j))
    for highest in pos:
        if visited[highest[0]][highest[1]]:
            continue
        cnt += 1
        ans += 1
        visited[highest[0]][highest[1]] = True
        dfs(highest[0],highest[1],arr[highest[0]][highest[1]])
print(ans)