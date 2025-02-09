class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        # n = len(nums)
        
        # total_sum = nums[0]
        # max_sum = nums[0]
        # min_sum = nums[0]
        # temp_max_sum = nums[0]
        # temp_min_sum = nums[0]
        # for i in range(1,n):
        #     total_sum+=nums[i]

        #     temp_max_sum = max(temp_max_sum+nums[i],nums[i])
        #     max_sum = max(temp_max_sum,max_sum)

        #     temp_min_sum = min(temp_min_sum+nums[i],nums[i])
        #     min_sum = min(temp_min_sum,nums[i])
        # circular_sum = total_sum-min_sum

        # if max_sum < 0:
        #     return max_sum
        # return max(max_sum,circular_sum)

        n = len(nums)
        total_sum = 0  # Initialize total_sum to 0
        max_sum = -float('inf') # Initialize max_sum to negative infinity
        min_sum = float('inf')  # Initialize min_sum to positive infinity
        temp_max_sum = 0 # Initialize temp_max_sum to 0
        temp_min_sum = 0 # Initialize temp_min_sum to 0

        for i in range(n):
            total_sum += nums[i]

            temp_max_sum = max(temp_max_sum + nums[i], nums[i])
            max_sum = max(temp_max_sum, max_sum)

            temp_min_sum = min(temp_min_sum + nums[i], nums[i])
            min_sum = min(temp_min_sum, min_sum)

        if max_sum < 0:  # Correctly handle all-negative case
            return max_sum

        circular_sum = total_sum - min_sum
        return max(max_sum, circular_sum)
        
