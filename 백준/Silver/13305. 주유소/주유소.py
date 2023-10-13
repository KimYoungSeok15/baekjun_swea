n = int(input())
dis = list(map(int, input().split()))
price = list(map(int, input().split()))
idx = n-1
ans = 0
while idx:
    ans += min(price[:idx])*dis[idx-1]
    idx -= 1
print(ans)