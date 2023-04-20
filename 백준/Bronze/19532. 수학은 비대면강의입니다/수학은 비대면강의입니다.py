a,b,c,d,e,f = map(int,input().split())
y = (f-c*d/a)/(e-b*d/a) if a else c/b
x = (c-b*y)/a if a else (f-c*e/b)/d
print(round(x), round(y))