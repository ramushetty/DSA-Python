def trapping(nums):
    # res =0 
    # n = len(nums)
    # for i in range(1,n-1):

    #     left_max = nums[i]

    #     for j in range(0,i):
    #         if nums[j] > left_max:
    #             left_max = nums[j]
        
    #     right_max = nums[i]

    #     for k in range(i,n):
    #         if nums[k] > right_max:
    #             right_max = nums[k]
        
    #     res += min(left_max,right_max) - nums[i]

    # return res
    n  = len(nums)
    res = 0
    left = [0]*n
    right = [0]*n

    left[0] = nums[0]
    for i in range(1,n):
        left[i] = max(left[i-1],nums[i])

    right[n-1] = nums[n-1]

    for i in range(n-2,-1,-1):
        right[i] = max(nums[i],right[i+1])

    for i in range(0,n):

        res += min(left[i],right[i]) - nums[i]

    return res

print(trapping([3, 1, 2, 0, 4]))