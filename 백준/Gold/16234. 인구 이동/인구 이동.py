from collections import deque
n, low, high = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
d = ((0,1),(0,-1),(1,0),(-1,0))
time_passed = 0
while True:
    done = False
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                q = deque([(i,j)])
                union = [(i,j)]
                sum_of_area = lst[i][j]
                while q:
                    r, c = q.popleft()
                    for dr, dc in d:
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and low <= abs(lst[r][c] - lst[nr][nc]) <= high:
                            q.append((nr,nc))
                            union.append((nr,nc))
                            visited[nr][nc] = True
                            sum_of_area += lst[nr][nc]
                new_pop = sum_of_area // len(union)
                for country in union:
                    row, col = country
                    lst[row][col] = new_pop
                if len(union) > 1:
                    done = True
    if not done:
        print(time_passed)
        break
    time_passed += 1    