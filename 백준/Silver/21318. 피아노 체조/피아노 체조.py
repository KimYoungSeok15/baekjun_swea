import sys

input = sys.stdin.readline
print = sys.stdout.write
N = int(input())
diff = list(map(int, input().split()))
Q = int(input())

miss = [0]
for i in range(N - 1):
    if diff[i] <= diff[i + 1]:
        new_miss = miss[-1]
    else:
        new_miss = miss[-1] + 1
    miss.append(new_miss)

for _ in range(Q):
    x, y = map(int, input().split())
    print(str(miss[y - 1] - miss[x - 1]) + "\n")
