class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        summ = nums[0]
        maxsum = nums[0]

        for i in range(1,n):
            summ = max(summ+nums[i],nums[i])
            maxsum = max(maxsum,summ)
        return maxsum
        