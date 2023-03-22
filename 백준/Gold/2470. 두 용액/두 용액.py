n = int(input())
liq = sorted(list(map(int, input().split())))
l, r = 0, n-1  # 양 끝단의 포인터
diff_min = 2*10**9
ans=(liq[l],liq[r])
while r!=l:  # 포인터가 만나기 전까지
    left, right = liq[l], liq[r]
    diff_now = abs(left+right)
    if diff_now < diff_min:
        diff_min = diff_now
        ans = (left, right)
    if abs(left)>abs(right):
        l += 1
    else:
        r -= 1
print(*ans)
    
