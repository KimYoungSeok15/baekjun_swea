n = int(input())
dices = [list(map(int, input().split())) for _ in range(n)]
num_pair = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}  # 맞은 편에 있는 숫자 구하기용. 0/5 1/3 2/4가 짝이다
rlt = []  # 밑면이 될 수 있는 6가지 경우의 수에 대해 결과 저장
for start in range(1,7):  # num : 첫 주사위의 윗면으로 놓일 숫자
    cnt = 0  # 카운트. 전체에서 빼줄 숫자
    top = start  # 현재 주사위의 윗면 숫자 저장용
    for i in range(n):  # 2층~ n층 주사위에 대해
        bot = top  # 이번 주사위의 밑면은 아래 주사위의 윗면
        top = dices[i][num_pair[dices[i].index(bot)]]  # 현재 주사위의 밑면의 인덱스를 받아 윗면의 숫자를 가져오는 과정
        if bot != 6 and top != 6:  # 6이 옆면으로 가능한 경우
            continue
        else:  # 6이 옆면으로 불가능한 경우
            if bot == 5 or top == 5:  # 5도 불가능한 경우
                cnt += 2  # 옆면이 4. 최댓값에서 2 감소
            else:  # 6은 불가능한데 5는 가능한 경우
                cnt += 1  # 옆면이 5. 최댓값에서 1 감소
        
    rlt.append(cnt)  # 결과값 저장
result = 6*n - min(rlt)  # 진짜 결과
print(result)
        