class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ = 0
        n = len(nums)
        maxi = float('-inf')
        for i in range(n):
            summ += nums[i]
            if summ > maxi:
                maxi = summ
            if summ < 0:
                summ = 0
        return maxi
        