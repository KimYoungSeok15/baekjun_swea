n , m =map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
for _ in range(k):
  i,j,x,y = map(int, input().split())
  s = 0
  for p in range(i-1,x):
    for q in range(j-1,y): 
      s += board[p][q]
  print(s)