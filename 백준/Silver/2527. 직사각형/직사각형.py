for tc in range(4):
    lst = list(map(int, input().split()))
    s1, s2 = lst[:4], lst[4:]
    tx = max(s1[2],s2[2])-min(s1[0],s2[0])
    ty = max(s1[3],s2[3])-min(s1[1],s2[1])
    if tx>s1[2]-s1[0]+s2[2]-s2[0] or ty>s1[3]-s1[1]+s2[3]-s2[1]:
        print('d')
    elif tx==s1[2]-s1[0]+s2[2]-s2[0] and ty==s1[3]-s1[1]+s2[3]-s2[1]:
        print('c')
    elif tx==s1[2]-s1[0]+s2[2]-s2[0] and ty<s1[3]-s1[1]+s2[3]-s2[1]:
        print('b')
    elif tx<s1[2]-s1[0]+s2[2]-s2[0] and ty==s1[3]-s1[1]+s2[3]-s2[1]:
        print('b') 
    else:
        print('a')       