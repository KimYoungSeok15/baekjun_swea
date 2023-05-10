def search(s,e,k):
    if s==e:
        return s
    mid = (s+e)//2
    if not mid%2:
        if  k<(mid//2)**2+mid//2:
            return search(s,mid,k)
        elif  k>(mid//2)**2+mid//2:
            return search(mid+1,e,k)
        else:
            return mid
        
    else:
        if  k<((mid-1)//2)**2+mid:
            return search(s,mid,k)
        elif  k>((mid-1)//2)**2+mid:
            return search(mid+1,e,k)
        else:
            return mid        
            
for _ in range(int(input())):
    x, y = map(int, input().split())
    print(search(1,(y-x)**2,y-x))