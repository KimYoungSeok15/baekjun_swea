def roll(x, t, size): # x: 현재 위치, t: 남은시간, size: 현재 사이즈
    global best
    if x > n:
        best = max(best, size)
        return
    size += snow[x]        
    if t == 0:
        best = max(best, size)
        return
    roll(x+1, t-1, size)
    size = size//2
    roll(x+2, t-1, size)
    
n, m = map(int, input().split())
snow = [0]+list(map(int, input().split()))
if m >= n:
    print(sum(snow)+1)
    exit()
best = 0
roll(0,m,1)
print(best)
