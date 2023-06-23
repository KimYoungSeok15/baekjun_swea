x, y = map(int, input().split())
def search(s,e,dif):
    if s == e:
        return s
    m = (s+e)//2
    if m%2:
        t = m//2+1
        cal = t*(t+1)//2+(t-1)*t//2
    else:
        t = m//2
        cal = t*(t+1)
    if cal >= dif:
        return search(s,m,dif)
    else:
        return search(m+1,e,dif)
print(search(0,2**31,y-x))