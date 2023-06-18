n = int(input())
arr = [input() for _ in range(n)]
best = 0

for i in range(n):
    
    friend = set()
    check = []
    two_friend = set()
    
    for j in range(n):
        
        if i == j:
            continue
        
        if arr[i][j] == 'Y':
            friend.add(j)
        
        else:
            check.append(j)
    
    for f in friend:
        
        for k in range(n):
            
            if k != i and arr[f][k] == 'Y':

                two_friend.add(k)

    two_friend.update(friend)
    best = max(best, len(two_friend))
print(best)