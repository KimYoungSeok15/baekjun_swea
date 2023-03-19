T = int(input())
for tc in range(1, 1+T):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    if (x1-x2)**2 + (y1-y2)**2 == 0 and r1 == r2 :
        print(-1)      
    elif (x1-x2)**2 + (y1-y2)**2 > (r1+r2)**2:
        print(0)
    elif (x1-x2)**2 + (y1-y2)**2 == (r1+r2)**2:
        print(1)
    elif (x1-x2)**2 + (y1-y2)**2 < (r1+r2)**2 and (x1-x2)**2 + (y1-y2)**2 > (max(r1,r2) - min(r1,r2))**2:
        print(2)        
    elif (x1-x2)**2 + (y1-y2)**2 < (r1+r2)**2 and (x1-x2)**2 + (y1-y2)**2 == (max(r1,r2) - min(r1,r2))**2:
        print(1) 
    elif (x1-x2)**2 + (y1-y2)**2 < (r1+r2)**2 and (x1-x2)**2 + (y1-y2)**2 < (max(r1,r2) - min(r1,r2))**2:
        print(0)    