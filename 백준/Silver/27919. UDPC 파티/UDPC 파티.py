a = input() 
cnt = [0,0]
for i in a:
    if i == 'U' or i == 'C':
        cnt[0] += 1
    else:
        cnt[1] += 1
        
if cnt[0] > (cnt[1]+1)//2 and cnt[1]:
    print('UDP')
elif cnt[1] == 0:
    print('U')
else:
    print('DP')