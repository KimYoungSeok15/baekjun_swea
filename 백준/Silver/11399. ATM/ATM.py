people = int(input())
people_list = []
people_list.extend(map(int, input().split()))
people_list.sort()
ans = 0
for idx in range(len(people_list)) :
    ans += sum(people_list[:idx+1])
print(ans)