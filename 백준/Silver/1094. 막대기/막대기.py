x = int(input())
lst = [64]
while sum(lst) > x:
    lst.extend([lst.pop(0)//2]*2)
    lst.sort()
    if sum(lst)-lst[0] >= x:
        lst.pop(0)
print(len(lst))