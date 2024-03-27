n = int(input())
schedules = [list(map(int, input().split())) for _ in range(n)]
schedules.sort(
    key=lambda x: (x[0], -x[1])
)  # 앞에 대해 오름차순 정렬하되 동률일 경우 뒤에 대해 내림차순 정렬

# 달력에 저장
calendar = [[] for _ in range(367)]
for schedule in schedules:
    s, e = schedule
    for i in range(s, e + 1):
        calendar[i].append(e)


# 코팅지 자르기
i = 0
streak = 0
height = 0
ans = 0
while i < 367:

    # 해당 일에 일정이 없다면
    if not calendar[i]:
        # 어제까지의 연속된 일정에 대한 코팅지 자르기
        ans += streak * height
        streak = 0
        height = 0

    # 일정이 있다면 길이 증가 및 높이 갱신(가능하다면)
    else:
        streak += 1
        height = max(height, len(calendar[i]))

    i += 1

print(ans)
