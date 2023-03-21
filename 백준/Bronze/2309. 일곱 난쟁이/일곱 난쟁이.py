lst = [int(input()) for _ in range(9)]
# 9개 중에 7개만 선택해서 생기는 부분집합들을 생성
comb = []
for i in range(1<<9):
    temp = []    
    for j in range(9):
        if i&1<<j:
            temp.append(j)
    if len(temp) == 7:
        comb.append(temp)
rlt = []
for n in comb:
    temp2 = []    
    for k in range(7):
        temp2.append(lst[n[k]])
    rlt.append(temp2)

# 부분집합 중에서 합이 100이면 정렬해서 출력
for m in rlt:
    if sum(m) == 100:
        m.sort()
        for l in range(7):
            print(m[l])
        exit()