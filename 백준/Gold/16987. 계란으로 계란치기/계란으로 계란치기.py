import sys
input = sys.stdin.readline
N = int(input())
eggs = [list(map(int, input().split())) for _ in range(N)]
ans = 0


def refresh_ans():
    global ans
    temp_ans = 0
    for i in range(N):
        if eggs[i][0] <= 0:
            temp_ans += 1
    ans = max(ans, temp_ans)


def dfs(idx):
    global ans

    # 종료조건
    if idx == N:
        refresh_ans()
        return

    # 이번 계란이 깨졌다면 다음 계란 확인
    if eggs[idx][0] <= 0:
        dfs(idx+1)
        return

    ever_broke = False  # 한번이라도 충돌을 했는지

    # 깨지지 않은 계란 재귀호출
    for i in range(N):

        # 현재 계란이 아니고 깨지지 않은 경우
        if i != idx and eggs[i][0] > 0:

            # 충돌
            eggs[idx][0] -= eggs[i][1]
            eggs[i][0] -= eggs[idx][1]

            # 재귀호출
            dfs(idx + 1)
            ever_broke = True

            # 원상복구
            eggs[idx][0] += eggs[i][1]
            eggs[i][0] += eggs[idx][1]

    # 다른 모든 계란이 깨졌다면
    if not ever_broke:
        refresh_ans()
        return


dfs(0)
print(ans)
