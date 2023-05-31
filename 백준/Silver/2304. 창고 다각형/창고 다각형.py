n = int(input())
column = [list(map(int, input().split())) for _ in range(n)]
column.sort()
max_idx = column.index(max(column, key = lambda x: x[-1]))
cnt = 0
if max(column, key = lambda x: x[-1]) == min(column, key = lambda x: x[-1]):
    print(column[0][1]*(column[0][0]-column[-1][0]+1))
    exit()

# 앞에서부터 max 인덱스까지
i = 0
while column[i][1] < column[max_idx][1]:
    j = 1
    while column[i][1]>=column[i+j][1]:   # 높이가 더 큰 기둥을 만나기 전까지
        j += 1
    cnt += column[i][1]*(column[i+j][0]-column[i][0])

    i += j
# 뒤에서부터 max 인덱스까지    
i = n-1
while column[i][1] < column[max_idx][1]:
    j = 1
    while column[i][1]>=column[i-j][1]:   # 높이가 더 큰 기둥을 만나기 전까지
        j += 1
    cnt += column[i][1]*(column[i][0]-column[i-j][0])
 
    i -= j
max_col = []
for c in column:
    if c[1] == column[max_idx][1]:
        max_col.append(c[0])
max_col.sort()
cnt += (max_col[-1]-max_col[0]+1) * column[max_idx][1]
print(cnt)
