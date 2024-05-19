N = int(input())
arr = [input() for _ in range(N)]

ans = ""


def solve(size, row, col):
    global ans
    if size == 1:
        ans += arr[row][col]
        return

    clear = True
    first = arr[row][col]

    for i in range(row, row + size):
        for j in range(col, col + size):
            if arr[i][j] != first:
                clear = False
                ans += "("
                for r in range(row, row + size, size // 2):
                    for c in range(col, col + size, size // 2):
                        solve(size // 2, r, c)
                ans += ")"
                break

        if not clear:
            break

    if clear:
        ans += first


solve(N, 0, 0)
print(ans)
