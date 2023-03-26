n, m = map(int,input().split())
log = list(map(int, input().split()))
def search(start, end):  # 최적의 높이를 찾는 함수
    if start == end : 
        return start
    height = (start + end) //2 + 1
    cnt = 0
    for l in log:
        if l > height:
            cnt += l-height
    if cnt >= m:  # 잘린 높이가 충분할 경우
        return search(height, end)  # 더 높은 높이에서 실행
    else:  # 잘린 높이가 부족 할 경우
        return search(start, height-1)  # 더 낮은 높이에서 실행
print(search(0, max(log)))