n = int(input())
member = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    temp = 0
    for j in range(n):
        if i!=j:
            if member[i][0] < member[j][0] and member[i][1] < member[j][1]:
                temp += 1
    print(temp+1, end=' ')
