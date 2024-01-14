from collections import deque
n, m = map(int, input().split())
ladder = [list(map(int, input().split())) for _ in range(n)]
snake = [list(map(int, input().split())) for _ in range(m)]
len_l = len(ladder)
len_s = len(snake)
v = [0]*101
q = deque([(1,0)])
while q:
    idx, ans = q.popleft()
    v[idx] = 1
    for i in range(1,7):
        nidx = idx + i
        if v[nidx]:
            continue
        
        if nidx == 100:
            print(ans+1)
            exit()
        
        for j in range(len_l):
            if nidx == ladder[j][0]:
                q.append([ladder[j][1], ans+1])
                break
        else:
            for j in range(len_s):
                if nidx == snake[j][0]:
                    q.append([snake[j][1], ans+1])
                    break
            else:
                q.append([nidx, ans+1])
            
    