board = [input().split() for _ in range(19)]
d = [(0, 1), (1, 1), (1, 0), (-1, 1)]
for r in range(19):
    for c in range(19):
        org = board[r][c]
        if org == "0":
            continue
        else:
            for dir in d:
                dr, dc = dir
                for i in range(1, 5):
                    nr, nc = r + dr * i, c + dc * i
                    if 0 <= nr < 19 and 0 <= nc < 19 and org == board[nr][nc]:
                        continue
                    else:
                        break
                else:
                    nr, nc = r + dr * 5, c + dc * 5
                    if (
                        (not 0 <= nr < 19)
                        or (not 0 <= nc < 19)
                        or (org != board[nr][nc])
                    ):
                        nr, nc = r - dr, c - dc
                        if (
                            (not 0 <= nr < 19)
                            or (not 0 <= nc < 19)
                            or (org != board[nr][nc])
                        ):
                            print(org)
                            print(r + 1, c + 1)
                            exit()
print(0)
