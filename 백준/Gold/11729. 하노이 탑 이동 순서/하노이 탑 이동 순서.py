n = int(input())

cnt = 2**n-1
print(cnt)

pool = set([1,2,3])

def move(f,t,k):
    
    if k == 1:
        print(f, t)
        return
    
    other = next(iter(pool-{f,t}))
    move(f,other,k-1)
    print(f,t)
    move(other,t,k-1)

move(1,3,n)
    