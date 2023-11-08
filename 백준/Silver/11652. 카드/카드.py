import sys
dic = {}
N = int(sys.stdin.readline())
for n in range(N):
    a = int(sys.stdin.readline())
    if a in dic.keys():
        dic[a] += 1
    else:
        dic[a] = 1

dic = sorted(dic.items(), key = lambda x: (-x[1], x[0]))
print(dic[0][0])
