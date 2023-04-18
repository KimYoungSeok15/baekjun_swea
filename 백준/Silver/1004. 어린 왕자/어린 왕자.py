T = int(input())
for tc in range(T):
    cnt = 0
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    for p in lst:
        if (x1-p[0])**2 + (y1-p[1])**2 < p[2]**2:
            cnt += 1
        if (x2-p[0])**2 + (y2-p[1])**2 < p[2]**2:
            cnt += 1
        if (x1-p[0])**2 + (y1-p[1])**2 < p[2]**2 and (x2-p[0])**2 + (y2-p[1])**2 < p[2]**2:
            cnt -= 2
    print(cnt)