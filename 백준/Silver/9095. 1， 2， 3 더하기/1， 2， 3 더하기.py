#바텀업 방식
T = int(input())
for tc in range(T):
    n = int(input())
    d = [set() for _ in range(n+1)]  # 겹치지 않도록 세트 이용
    d[1] = {'1'}  # 1~3은 선언
    if n>1:
        d[2] = {'11', '2'}
        if n>2:
            d[3] = {'111', '12', '21', '3'}
    for i in range(4, n+1):  # 4 이상부터 n까지 앞뒤에 1,2,3 붙임
        for item in d[i-3]:
            d[i].add(item+'3')
            d[i].add('3'+item)
        for item in d[i-2]:
            d[i].add(item+'2')
            d[i].add('2'+item)      
        for item in d[i-1]:
            d[i].add(item+'1')
            d[i].add('1'+item)                  
    print(len(d[n]))