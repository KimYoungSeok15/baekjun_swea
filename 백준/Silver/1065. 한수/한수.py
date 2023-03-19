n = input()
if int(n)<100:
    print(n)
    exit()
cnt = 99
for i in range(100, int(n)+1):
    string = str(i)
    for j in range(len(string)-2):
        if int(string[j]) - int(string[j+1]) == int(string[j+1]) - int(string[j+2]):
            continue
        break
    else:
        cnt += 1
print(cnt)