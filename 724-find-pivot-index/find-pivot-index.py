class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = 0
        for element in nums:
            total_sum += element
        
        cum_sum = 0
        for index in range(len(nums)):
            right_sum = total_sum - cum_sum - nums[index]
            if cum_sum == right_sum:
                return index
            cum_sum += nums[index]

        return -1
        