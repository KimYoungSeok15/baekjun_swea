import sys
input = sys.stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
max_dp = [board[0][0],board[0][1],board[0][2]]
min_dp = [board[0][0],board[0][1],board[0][2]]
for row in range(1,n):
    max_dp[0], max_dp[1], max_dp[2] = max(max_dp[0], max_dp[1]) + board[row][0], max(max_dp[0], max_dp[1], max_dp[2]) + board[row][1], max(max_dp[1], max_dp[2]) + board[row][2]
    min_dp[0], min_dp[1], min_dp[2] = min(min_dp[0], min_dp[1]) + board[row][0], min(min_dp[0], min_dp[1], min_dp[2]) + board[row][1], min(min_dp[1], min_dp[2]) + board[row][2]
print(max(max_dp), min(min_dp))