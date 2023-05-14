n, s = map(int, input().split())
lst = list(map(int, input().split()))
left, right = 0, 0
ans = 100001
sum_now = lst[0]
while True:
    if sum_now >= s:
        ans = min(ans, right-left + 1)
        if ans == 1:
            print(1)
            exit()
        sum_now -= lst[left]
        left += 1
    else:
        if right < n-1:
            right += 1
            sum_now += lst[right]
        else:
            if ans == 100001:
                print(0)
            else:
                print(ans)
            exit()