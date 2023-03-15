nums = [input().split() for _ in range(5)]
num_set = set()
for i in range(5):
    for j in range(5):
        temp_set = set()
        stack = [ [ i, j, nums[i][j] ] ]
        for _ in range(5):
            temp_list = []            
            for item in stack:
                r, c, num = item[0], item[1], item[2]
                for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                    if 0<=r+dr<5 and 0<=c+dc<5:
                        temp_list.append([r+dr, c+dc, num+nums[r+dr][c+dc]])
            stack = temp_list[:]
        for number in stack:
            num_set.add(number[2])
print(len(num_set))
                        
            