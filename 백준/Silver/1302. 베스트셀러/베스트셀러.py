a = {}
for _ in range(int(input())):
    t = input()
    try:
        a[t] += 1
    except:
        a[t] = 1
mval = max(a.values())
temp = []
for i in a:
    if a[i] == mval:
        temp.append(i)
temp.sort()
print(temp[0])
