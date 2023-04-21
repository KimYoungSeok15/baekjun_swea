import math
a, b = map(int, input().split())
c, d = map(int, input().split())
while True:
    t = math.gcd(a,b)
    if t != 1:
        a, b = a//t, b//t
        continue
    else:
        break
while True:
    t = math.gcd(c,d)
    if t != 1:
        c, d = c//t, d//t
        continue
    else:
        break
e, f = a*d + c*b, b*d
while True:
    t = math.gcd(e,f)
    if t != 1:
        e, f = e//t, f//t
        continue
    else:
        break
print(e, f)