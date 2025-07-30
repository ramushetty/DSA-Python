class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total_sum = 0
        for ele in nums:
            total_sum += ele
        n = len(nums)
        ideal_sum = (n*(n+1))//2
        return ideal_sum - total_sum
        