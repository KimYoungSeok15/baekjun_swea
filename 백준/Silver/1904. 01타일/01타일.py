N = int(input())

# DP
cache = [0] * 1000001
cache[1] = 1
cache[2] = 2

for i in range(3, N+1):
    cache[i] = (cache[i-1] + cache[i-2]) % 15746
print(cache[N])