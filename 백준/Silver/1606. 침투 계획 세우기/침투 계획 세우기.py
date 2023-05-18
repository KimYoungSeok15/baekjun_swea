x, y = map(int, input().split())
# n번째 껍질의 원소 수(n^2-n)/2+4n-3
# n번째 껍질은 x=n-1에 n개의 원소를 만들고, x=n-1 까지는 2개의 원소를 만든다.
if x >= 0:
    cnt = 0
    while not -x<=y<=0:
        if y>0:
            y-=1
            cnt-=1
        else:
            y+=1
            cnt+=1
if x < 0:
    cnt = 0
    while not 0<=y<=-x:
        if y>0:
            y-=1
            cnt-=1
        else:
            y+=1
            cnt+=1

shell = x+1 + abs(cnt)  # 몇번째 껍질인지 알아낸다.
y = -cnt # shell 구했다면 y값 초기화
i = shell-2  # 탐색시작할 x좌표
j = 1  # 탐색 시작할 y좌표
now = 3*shell**2-9*shell+8 # 현재 위치의 숫자
# 원점은 예외처리
if x==0 and y==0:
    print(1)
    exit()

# 탐색 시작
while i != 0:
    if i == x and j == y:
        print(now)
        exit()
    else:
        i-=1
        j+=1
        now += 1

while i != 1-shell:
    if i == x and j == y:
        print(now)
        exit()
    else:
        i-=1
        now += 1

while j != 0:
    if i == x and j == y:
        print(now)
        exit()
    else:
        j -= 1
        now += 1        

while i != 0:
    if i == x and j == y:
        print(now)
        exit()
    else:
        i += 1
        j -= 1
        now += 1            
           
while i != shell-1:
    if i == x and j == y:
        print(now)
        exit()
    else:
        i+=1
        now += 1

while True:
    if i == x and j == y:
        print(now)
        exit()
    else:
        j+=1
        now += 1
