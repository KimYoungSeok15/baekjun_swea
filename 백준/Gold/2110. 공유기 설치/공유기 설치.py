n, c = map(int, input().split())
lst = sorted([int(input()) for _ in range(n)])
def binary(s,e):
    if s == e:
        return s
    mid = (s+e+1)//2
    cnt = 1
    idx = 0
    while True:  # 공유기 수가 c가 되거나 끝에 다다른 경우 종료
        i = 1
        while idx+i < n:
            if lst[idx+i] - lst[idx] >= mid:
                cnt += 1
                break
            i += 1
        if cnt == c or idx+i >= n:
            break
        idx += i
    if cnt == c: # 가능하다면
        return binary(mid,e)
    else:  # 불가능하다면
        return binary(s,mid-1)
print(binary(1,(lst[-1]-lst[0])//(c-1)+1))