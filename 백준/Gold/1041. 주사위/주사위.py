n = int(input())
nums_org = list(map(int, input().split()))
nums = sorted([min(nums_org[0],nums_org[5]),min(nums_org[1],nums_org[4]),min(nums_org[2],nums_org[3])])
nums = [nums[0],nums[0]+nums[1],sum(nums)]
print((n-2)*(5*n-6)*nums[0]+(4*n-4+4*n-8)*nums[1]+4*nums[2]) if n>=2 else print(sum(nums_org)-max(nums_org))