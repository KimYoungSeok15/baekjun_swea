for _ in range(int(input())):
    p = list(input())
    n = int(input())
    arr = list(map(int, input()[1:-1].replace(',',' ').split()))
    going_right = True
    now_idx = 0
    D_cnt = 0
    left_del = 0
    right_del = 0
    for char in p:
        if char == 'R':
            now_idx = left_del if going_right == False else n-1-right_del
            going_right = True if going_right == False else False
        else:
            D_cnt += 1
            if D_cnt > n:
                print('error')
                break
            if going_right == True:
                now_idx += 1
                left_del += 1
            else:
                now_idx -= 1
                right_del += 1
    else:
        print('[]' if D_cnt == n else str(arr[now_idx:n-right_del]).replace(' ','') if going_right == True else str(arr[now_idx:left_del-1:-1]).replace(' ','') if left_del else str(arr[now_idx:0:-1]).replace(' ','')[:-1]+','+str(arr[0])+']' if len(arr) > 1 else str(arr))