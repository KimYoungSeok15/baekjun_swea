n = int(input())
arr = list(map(int, input().split()))
s = sum(arr)
ans = 0
for num in arr:
    ans += num*(s-num)
ans = ans//2
print(ans%1000000007)