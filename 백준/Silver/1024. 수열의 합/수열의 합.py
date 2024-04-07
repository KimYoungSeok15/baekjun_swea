n, l = map(int, input().split())

for length in range(l, 101):
    a = n / length - (length - 1) / 2
    if a.is_integer() and a >= 0:
        start = int(a)
        result = list(range(start, start + length))
        print(*result)
        exit()

print(-1)
