n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
map_ = [[0]*1001 for _ in range(1001)]
for k in range(n):
    for i in range(paper[k][0],paper[k][0]+paper[k][2]):
        for j in range(paper[k][1],paper[k][1]+paper[k][3]):
            map_[i][j] = k+1
cnt = [0]*(n+1)
for r in range(1001):
    for c in range(1001):
        if map_[r][c]:
            cnt[map_[r][c]] += 1
for m in range(1,n+1):
    print(cnt[m]) 
