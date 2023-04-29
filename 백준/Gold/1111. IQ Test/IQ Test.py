import math
n = int(input())
arr = list(map(int, input().split()))
ans = []
if n >= 3:
    b1 = arr[1] - arr[0]
    if not b1 == 0:
        br = (arr[2] - arr[1]) / b1
    else:
        for i in range(1,n):
            if arr[i] != arr[0]:
                print('B')
                exit()
        print(arr[0])
        exit()
    if math.isclose(br,int(br)):
        br = int(br)
    else:
        print('B')
        exit()
    i = 0
    while i <= n-2:
        if arr[i+1] == arr[i] + b1*br**i:
            i += 1
            continue
        else:
            print('B')
            exit()
    print(arr[n-1] + b1*br**(n-1))
elif n==2 and arr[0] == arr[1]:
    print(arr[0])

else:
    print('A')