n = int(input())
lst = list(map(int, input().split()))
s = int(input())
for i in range(n-1):
    if s == 0:
        break
    max_num = lst[i]
    j = 1     
    while i+j < n and j<=s:  # 끝까지 또는 s만큼
        if max_num < lst[i+j]:  # 최댓값과 그때의 인덱스 차이를 구한다
            max_num = lst[i+j]
            idx_dif = j
        j += 1
    if lst[i] == max_num:  # 바꿀 게 없다면
        continue
    lst.insert(i, lst.pop(i+idx_dif))
    s -= idx_dif
print(*lst)