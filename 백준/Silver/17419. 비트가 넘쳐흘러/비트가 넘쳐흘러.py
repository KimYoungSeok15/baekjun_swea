N = input()
K = int(input(), 2) # 2진수
cnt = 0
while K:
  K = K-(K&((~K)+1))
  cnt += 1
print(cnt)