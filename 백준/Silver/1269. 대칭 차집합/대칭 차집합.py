a, b = map(int, input().split())
arr1 = set(map(int, input().split()))
arr2 = set(map(int, input().split()))
union = arr1.intersection(arr2)
A = arr1.difference(union)
B = arr2.difference(union)
print(len(A)+len(B))