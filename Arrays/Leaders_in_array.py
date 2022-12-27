def leaders(nums):
    n = len(nums)-1
    max = 0
    for i in range(n,-1,-1):
        if max < nums[i]:
            max = nums[i]
            print(max,end=" ")
    
nums = [5,3,20,15,8,3]
leaders(nums)

