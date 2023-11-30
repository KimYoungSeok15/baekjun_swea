n, r, c = map(int, input().split())
row_s, row_e = 0, 2**(n)-1
col_s, col_e = 0, 2**(n)-1
cnt = 0
while n>1:
    if r<=(row_s + row_e)//2:
        row_e = (row_s + row_e)//2
    else:
        row_s = (row_s + row_e)//2+1
        cnt += 2**(2*n-1)
    if c<=(col_s + col_e)//2:
        col_e = (col_s + col_e)//2
    else:
        col_s = (col_s + col_e)//2+1
        cnt += 2**(2*n-2)
    n -= 1
if not r%2 and not c%2:
    pass
if not r%2 and c%2:
    cnt += 1
if r%2 and not c%2:
    cnt += 2
if r%2 and c%2:
    cnt += 3

print(cnt)