n = int(input())
lst = list(map(int, input().split()))
ans = 0
for i in range(n): # 각 빌딩 검사
    cnt = 0  # 현재 빌딩 카운트
    for left in range(i):  # 현재 빌딩 맨 왼쪽부터, 중간에 걸리는게 없는지 조사
        gradient = (lst[i] - lst[left]) / (i - left)  # left ~ i 기울기
        for mid in range(left+1, i): 
            if (lst[mid] - lst[left]) / (mid - left) >= gradient:  # left ~ mid의 기울기가 gradient보다 크다면 pass, 아니면 cnt += 1
                break
        else:  # 중간 모든 값들이 문제없다면
            cnt += 1
    for right in range(i+1, n):
        gradient = (lst[i] - lst[right]) / (i - right)  # i ~ right 기울기
        for mid in range(i+1, right): 
            if (lst[mid] - lst[right]) / (mid - right) <= gradient:  # right ~ mid의 기울기가 gradient보다 크거나 같으면 pass, 아니면 cnt += 1
                break
        else: # 중간 모든 값들이 문제없다면
            cnt += 1
    ans = max(ans, cnt)
print(ans)