n = int(input())
arr = list(map(int, input().split()))
s = []
ans = [0]*n
i = 0
l = 0
while i < n:
    while l:
        if s[l-1][0] < arr[i]:
            ans[s[l-1][1]] = arr[i]
            s.pop()
            l -= 1
        else:
            break
    s.append([arr[i],i])
    l += 1
    i += 1
ans[n-1] = -1
for i in range(l-1):
    ans[s[i][1]] = -1
print(*ans)