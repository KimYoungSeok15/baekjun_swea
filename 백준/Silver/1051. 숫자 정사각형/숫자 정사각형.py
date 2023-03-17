n, m = map(int,input().split())
lst = [list(map(int, input())) for _ in range(n)]
best = 0
for r in range(n):
    for c in range(m):
        size = 1  # 정사각형의 한 변의 길이. 실제 길이는 size + 1
        while r+size < n and c+size < m:  # 남동 방향으로 확인
            if lst[r][c] == lst[r+size][c] == lst[r][c+size] == lst[r+size][c+size]:
                best = max(best, size)
            size += 1

print((best+1)**2)
