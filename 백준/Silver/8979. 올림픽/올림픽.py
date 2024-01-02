n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    if arr[i][0] == k:
        g, s, b = arr[i][1:]
        
cnt = 1
        
for i in range(n):
    G, S, B = arr[i][1:]
    if not arr[i][0] == k:
        if G > g:
            cnt += 1
        elif G == g and S > s:
            cnt += 1
        elif G == g and S == s and B > b:
            cnt += 1

print(cnt)