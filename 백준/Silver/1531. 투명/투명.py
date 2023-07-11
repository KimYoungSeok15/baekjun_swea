n , m = map(int, input().split())
paper = [list(map(lambda x:int(x)-1, input().split())) for _ in range(n)]
pic = [[0]*101 for _ in range(101)]
for p in paper:
    for x in range(p[0],p[2]+1):
        for y in range(p[1],p[3]+1):
            pic[x][y] += 1
ans = 0
for i in range(101):
    for j in range(101):
        if pic[i][j]>m:
            ans += 1

print(ans)