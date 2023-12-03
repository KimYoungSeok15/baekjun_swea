n = int(input())
lst = list(input())

d = [0]*n
for i in range(n):
    d[i] = int(input())

for i in range(len(lst)):
    if lst[i].isalpha():
        lst[i] = d[ord(lst[i])-65]
        
s = []

for j in range(len(lst)):
    t = lst[j]
    if not s or str(t).isdigit():
        s.append(t)
    elif t == '*':
        s.append(s.pop()*s.pop())
    elif t == '/':
        temp = s[-2]/s[-1]
        s.pop()
        s.pop()
        s.append(temp)
    elif t == '+':
        s.append(s.pop()+s.pop())
    else:
        temp = s[-2]-s[-1]
        s.pop()
        s.pop()
        s.append(temp)

print("{:.2f}".format(s[0]))