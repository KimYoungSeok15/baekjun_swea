import math

N, M = map(int, input().split())
arr = [input() for _ in range(N)]
ans = -1


def is_square_num(n):
    return math.isclose(math.isqrt(n) ** 2, n)


# 모든 점에 대해 실행
for r in range(N):
    for c in range(M):
        num = arr[r][c]

        # 시작점이 홀로 완전수인지 확인
        if is_square_num(int(num)):
            ans = max(ans, int(num))

        # 가능한 모든 r과 c의 변화에 대해
        for dr in range(-r, N - r):
            for dc in range(-c, M - c):

                # 둘다 0인 경우는 예외처리
                if dr == dc == 0:
                    pass

                else:
                    d = 1
                    res = num

                    # 영역 내에서 모두 붙인다
                    while 0 <= r + dr * d < N and 0 <= c + dc * d < M:
                        res += arr[r + dr * d][c + dc * d]
                        if is_square_num(int(res)):
                            ans = max(ans, int(res))
                        d += 1

print(ans)
