a = input()
s = set()
for leng in range(1,len(a)+1):
    for i in range(len(a)-leng+1):
        s.add(a[i:i+leng])
print(len(s))