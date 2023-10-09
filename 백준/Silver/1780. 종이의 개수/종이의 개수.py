import sys
input = sys.stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ans = dict()
ans[-1] = 0
ans[0] = 0
ans[1] = 0
def check(i, j, size):
    temp = []
    for r in range(i, i+size):
        for c in range(j, j+size):
            if temp and temp[0] != board[r][c]:
                for a in range(i,i+size,size//3):
                    for b in range(j,j+size,size//3):
                        check(a, b, size//3)
                return
            
            temp = [board[r][c]]
    ans[board[i][j]] += 1
    
check(0, 0, n)
print(ans[-1])
print(ans[0])
print(ans[1])