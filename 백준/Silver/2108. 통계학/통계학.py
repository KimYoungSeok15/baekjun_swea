from sys import stdin
input = stdin.readline
n = int(input())
m = [0]*8001
summ = 0
for _ in range(n):
    num = int(input())
    m[num+4000] += 1
    summ += num

print(round(summ/n))

cnt = 0
for i in range(8001):
    cnt += m[i]
    if cnt > n//2:
        print(i-4000)
        break

for i in range(8001):
    if m[i]:
        small = i
        break
for i in range(8000,-1,-1):
    if m[i]:
        big = i
        break
    
temp = max(m)
if m.count(temp) == 1:
    print(m.index(temp)-4000)
else:
    m[m.index(temp)] = 0
    print(m.index(temp)-4000)

print(big-small)

