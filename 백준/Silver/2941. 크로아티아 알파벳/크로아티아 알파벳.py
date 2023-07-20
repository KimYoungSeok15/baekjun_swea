word = input()
d = {1 : 'c=', 2 : 'c-', 3 : 'dz=', 4 : 'd-', 5 : 'lj', 6 : 'nj', 7 : 's=', 8 : 'z='}
i = 0
ans = 0
while i < len(word):
    if word[i:i+2] in d.values():
        i += 2
    elif word[i:i+3] in d.values():
        i += 3
    else:
        i += 1
    ans += 1
print(ans)