class Solution:
    def rob(self, nums: List[int]) -> int:

        a = 0
        b = 0
        for i in range(len(nums)):
            a,b = b, max(nums[i]+a,b)
        return b