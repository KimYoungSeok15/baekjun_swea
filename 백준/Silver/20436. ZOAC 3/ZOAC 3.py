sl, sr = input().split()

# 키와 값의 대응 관계를 담은 딕셔너리 생성
dl = {
    "q": (0, 0),
    "w": (0, 1),
    "e": (0, 2),
    "r": (0, 3),
    "t": (0, 4),
    "a": (1, 0),
    "s": (1, 1),
    "d": (1, 2),
    "f": (1, 3),
    "g": (1, 4),
    "z": (2, 0),
    "x": (2, 1),
    "c": (2, 2),
    "v": (2, 3),
}

dr = {
    "y": (0, 1),
    "u": (0, 2),
    "i": (0, 3),
    "o": (0, 4),
    "p": (0, 5),
    "h": (1, 1),
    "j": (1, 2),
    "k": (1, 3),
    "l": (1, 4),
    "b": (2, 0),
    "n": (2, 1),
    "m": (2, 2),
}

left_row, left_col = dl[sl]
right_row, right_col = dr[sr]

command = input()
ans = len(command)
for char in command:
    if char in dl.keys():
        ans += abs(left_row - dl[char][0]) + abs(left_col - dl[char][1])
        left_row = dl[char][0]
        left_col = dl[char][1]
    else:
        ans += abs(right_row - dr[char][0]) + abs(right_col - dr[char][1])
        right_row = dr[char][0]
        right_col = dr[char][1]

print(ans)
