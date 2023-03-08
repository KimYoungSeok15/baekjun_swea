n = int(input())
cr = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))
cr.sort(reverse=True)
box.sort(reverse=True)
cnt = 0
if cr[0]<box[0]:
    print(-1)
else:
    while box:  # 모두 옮길 때 까지 계속 시도     
        for c in cr:
            if not box:
                break
            for b in box:  # 현재 크래인이 옮길 수 있는 가장 무거운 박스 옮긴다
                if c>=b: 
                    box.remove(b)
                    break  # 이후 박스는 스킵
            else:  # 현재 크래인이 옮길 수 있는 박스가 없다면
                break  # 시간 절약용. 이후 크래인 보지 말자.
        cnt += 1
    print(cnt)