n = int(input())
ans = 0
for _ in range(n):
    word = input()
    memo = []
    temp = ''
    for i in range(len(word)):
        if word[i] == temp:
            continue
        elif word[i] not in memo:
            memo.append(temp)
            temp = word[i]
        else:
            break
    else:
        ans += 1
print(ans)
    