import sys
T = int(input())
k = int(input())
coin = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(k)], reverse=True)
cnt = 0
dp = [1] + [0]*T
for c in coin:  # 각 동전에 대해
    for i in range(T,-1,-1):  # dp 테이블의 모든 인덱스에 대해 실행    
        for value in range(c[1],0,-1):  # 그 동전을 몇번 사용할 지에 대한 모든 경우의 수에 대해
            if dp[i] and i+c[0]*value <= T:
                dp[i+c[0]*value] += dp[i]
print(dp[-1])
