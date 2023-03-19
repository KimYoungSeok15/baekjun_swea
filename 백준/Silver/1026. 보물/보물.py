n= int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())), reverse=True)
summation = 0
for i in range(n):
    summation += a[i]*b[i]
print(summation)