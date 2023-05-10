n = input()  # str
ans = [0]*10

ans[0] -=  (len(n)-1)*10**(len(n)-2) + 10**(len(n)-1) if len(n) > 1 else 1 # 첫 시행에서 맨 앞자리에 0이 오는 경우의 수 빼주기. 한 글자일 경우 마지막에 0이 올 수 없으므로 -1만
for i in range(1, len(n)-1):  # 현재 자리수가 되기까지 필요한 0의 수
    ans[0] += i*9*10**(i-1)
    
def get(n): # n의 맨 앞자리 수를 떼면서 숫자들을 세는 함수  ex) 4321234 -> 321234
    
    global ans 
        
    lst = list(map(int, n))
    l = len(n)
    
    if len(n) == 1:  # n이 한자리 수 인 경우 탈출
        for i in range(int(n)+1):
            ans[i] += 1
        print(*ans)
        exit()
    
    temp1 = 0  # 0 의 횟수 카운트용
    temp2 = 0  # 1~9 의 횟수 카운트용
    
    for i in range(1, l):  # 현재 자리수가 되기까지 필요한 수
        temp2 += 10**(i-1) + (9*10**(i-2)*(i-1) if i>=2 else 0)

    temp2 +=  (lst[0]-1)*10**(l-2)*(l-1)  # 현재 수의 맨 앞자리수를 만들기까기 필요한 수  
    for i in range(1,10): # 맨 앞 자리수에 숫자 i가 들어갈 수 있는지 확인 후 ans[i]에 반영
        ans[i] += temp2  + (10**(l-1) if lst[0]-1 >= i else 0)      
        
    temp1 +=  (lst[0])*10**(l-2)*(l-1)  # 현재 수의 맨 앞자리수를 만들기까기 필요한 수
    ans[0] += temp1 + (10**(l-1) if lst[0] else 0)  # 앞자리에 0이 아닐때 0이 들어가는 경우. 앞자리가 이미 0인 경우는 아래에서 고려.

    ans[lst[0]] += int(n[1:])+1 # 자리수 이동 전에, 맨 앞 자리의 수는 뒤의 수 만큼 반복되므로
    get(n[1:])

get(n)

    