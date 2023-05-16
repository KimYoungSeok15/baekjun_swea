m = int(input())
lst1 = sorted(list(map(int, input().split())))
n = int(input())
lst2 = list(map(int, input().split()))
def search(s,e,k):
    if s >= e and lst1[s] != k:
        return 0
    mid = (s+e)//2
    if k == lst1[mid]:
        return 1
    elif k > lst1[mid]:
        return search(mid+1,e,k)
    else:
        return search(s,mid-1,k)
for i in lst2:
    print(search(0,m-1,i), end=' ')
print()