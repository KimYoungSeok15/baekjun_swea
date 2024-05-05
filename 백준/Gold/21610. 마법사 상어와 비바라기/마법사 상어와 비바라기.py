import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
commands = [list(map(int, input().split())) for _ in range(M)]

delta = ((), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1))
diag_delta = ((1, 1), (1, -1), (-1, 1), (-1, -1))
clouds = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]
for d, s in commands:
    dr, dc = delta[d]
    rained = []

    # 1 ~ 3
    for r, c in clouds:
        # 1
        nr, nc = (r + dr * s) % N, (c + dc * s) % N
        # 2
        board[nr][nc] += 1
        rained.append((nr, nc))

    # 4
    for r, c in rained:
        cnt = 0
        for dr, dc in diag_delta:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and board[nr][nc]:
                cnt += 1

        board[r][c] += cnt

    # 5
    clouds = []
    for r in range(N):
        for c in range(N):
            if board[r][c] >= 2 and (r, c) not in rained:
                clouds.append((r, c))
                board[r][c] -= 2


ans = 0
for i in range(N):
    for j in range(N):
        ans += board[i][j]
print(ans)

