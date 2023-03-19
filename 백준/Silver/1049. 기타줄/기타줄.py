n, m = map(int, input().split())
shop = [list(map(int, input().split())) for _ in range(m)]
six = min([i[0] for i in shop])
one = min([i[1] for i in shop])
six = min(six, one*6)
cnt = (n // 6) * six
cnt += one*(n%6) if one*(n%6) < six else six
print(cnt)