n = int(input())
lst = sorted(list(map(int, input().split())))
x = int(input())
left, right = 0, n-1
cnt = 0
while left < right:
    if lst[left] + lst[right] > x:
        right -= 1
        continue
    elif lst[left] + lst[right] < x:
        left += 1
        continue
    left, right, cnt = left + 1, right - 1, cnt + 1
print(cnt)