n = int(input())
if n == 0:
    print(0)
    exit()
dp = [1,1]
for i in range(n-2):
    dp.append(dp[i]+dp[i+1])
print(dp[-1])