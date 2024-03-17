arr = [list(map(int, input().split())) for _ in range(10)]
pos = []
for i in range(10):
    for j in range(10):
        if arr[i][j]:
            pos.append((i,j))

l = len(pos)
ans = 26
paper = [5]*5  # 남은 종이

def solve(idx): #  idx: pos기준 인덱스. cnt: 현재까지 가린 수
    global ans
    if idx == l:  # 모든 점을 가렸다면
        ans = min(ans, 25 - sum(paper))
        return
    
    r, c = pos[idx] #  현재 위치
    if not arr[r][c]: #  이미 지워진 곳이라면
        solve(idx+1)
        return
    
    for i in range(5): # 남은 종이에 대해
        if paper[i] and r+i<10 and c+i<10:
            for row in range(i+1):
                for col in range(i+1):
                    if not arr[r+row][c+col]:
                        break
                else:
                    continue
                break
            else:  # 놓을 수 있다면
                for row in range(i+1):  # 1 제거
                    for col in range(i+1):
                        arr[r+row][c+col] = 0
                        
                paper[i] -= 1
                solve(idx+1)
                paper[i] += 1
                
                for row in range(i+1):  # 원복
                    for col in range(i+1):
                        arr[r+row][c+col] = 1
                      
solve(0)
                        
if ans == 26:
    print(-1)
else:
    print(ans)