num = input()
m = [0]*10
for i in num:
  m[int(i)] += 1
m[6] += m[9]
m[6] = int(m[6]) // 2 if not int(m[6])%2 else int(m[6]) //2 + 1
m = m[:-1]
print(max(m))