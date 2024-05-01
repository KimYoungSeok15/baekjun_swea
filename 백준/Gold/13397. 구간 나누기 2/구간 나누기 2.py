N, M = map(int, input().split())
arr = [*map(int, input().split())]


# 가능한 최댓값을 찾는 함수
def search(s, e):
    if s > e:
        return s

    mid = (s + e) // 2

    cnt = 1  # 구간의 수
    idx = 1  # arr 순회 인덱스
    low = high = arr[0]
    while idx < N:
        low = min(low, arr[idx])
        high = max(high, arr[idx])

        # 새로운 구간이 형성되어야 할 경우
        if high - low > mid:
            cnt += 1

            # 불가능
            if cnt > M:
                break

            # 가능
            low = high = arr[idx]

        idx += 1
    # 가능
    else:
        return search(s, mid - 1)
    # 불가능
    return search(mid + 1, e)


print(search(0, 10000))
