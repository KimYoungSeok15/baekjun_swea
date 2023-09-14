from itertools import combinations
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = int(1e9)
all = range(n)
for team1 in combinations(range(n),n//2):
  team2 = []
  score = [0, 0]
  for i in all:
    if i not in team1:
      team2.append(i)
  for comb in combinations(team1, 2):
    score[0] += arr[comb[0]][comb[1]]
    score[0] += arr[comb[1]][comb[0]]
  for comb in combinations(team2, 2):
    score[1] += arr[comb[0]][comb[1]]
    score[1] += arr[comb[1]][comb[0]]
  ans = min(ans, abs(score[0]-score[1]))
print(ans)