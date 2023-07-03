n = int(input())
temp = n
k = -1
while temp:
    temp = temp // 3
    k += 1
    
board = [['*']*n for _ in range(n)]
while k:
    step = 3**(k-1)
    count = (n//3**k)
    for i in range(count):
        for j in range(count):
            for line in board[i*3*step + step : i*3*step + 2*step]:
                line[j*3*step + step : j*3*step + 2*step] = [' ']*step
    k -= 1
            
for line in board:
    for ele in line:
        print(ele, end='')
    print()