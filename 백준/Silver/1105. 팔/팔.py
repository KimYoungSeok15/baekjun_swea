l, r = input().split()
if len(l) != len(r):
    print(0)
    exit()
    
cnt = 0

i = 0
while i < len(l):
    if l[i] == r[i]:
        if l[i] == '8':
            cnt += 1
            i += 1
            continue
        else:
            i += 1
            continue
    break

print(cnt)