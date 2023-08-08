n = int(input())
arr1 = sorted(list(map(int, input().split())))
m = int(input())
arr2 = list(map(int, input().split()))

def search(s,e,k):
    if s > e:
        return 0
    
    mid = (s+e)//2
    if arr1[mid] > k:
        return search(s, mid-1, k)
    elif arr1[mid] < k:
        return search(mid+1, e, k)
    else:
        return 1

for num in arr2:
    print(search(0, n-1, num))