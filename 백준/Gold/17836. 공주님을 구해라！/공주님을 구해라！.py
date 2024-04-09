from collections import deque
n, m, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
d = ((1, 0), (0, 1), (-1, 0), (0, -1))
v = [[0] * m for _ in range(n)]
ans = int(1e9)
to_gram_time, gram_row, gram_col = int(1e9), 0, 0
q = deque([(0, 0)])
while q:
    r, c = q.popleft()
    now = v[r][c]
    if now == t:
        continue
    for dr, dc in d:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m and not v[nr][nc] and arr[nr][nc] != 1:
            v[nr][nc] = now + 1
            if nr == n - 1 and nc == m - 1:
                ans = now + 1
            elif arr[nr][nc] == 2:
                gram_row, gram_col, to_gram_time = nr, nc, now + 1
            q.append((nr, nc))

from_gram_time = to_gram_time + abs(gram_row - (n - 1)) + abs(gram_col - (m - 1))
ans = min(ans, from_gram_time)
if ans <= t:
    print(ans)
else:
    print("Fail")
