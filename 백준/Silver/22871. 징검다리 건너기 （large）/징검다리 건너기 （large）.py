N = int(input())
Ai = list(map(int, input().split()))
inf = int(1e9)


def search(s, e):
    if s > e:
        return s
    mid = (s + e) // 2
    possible = [0]
    for j in range(1, N):
        for i in possible:
            if mid >= (j - i) * (1 + abs(Ai[i] - Ai[j])):
                possible.append(j)
                break

    if possible[-1] == N - 1:
        return search(s, mid - 1)

    else:
        return search(mid + 1, e)


print(search(1, int(1e6)))
