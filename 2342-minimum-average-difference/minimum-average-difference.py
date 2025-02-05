class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        total_sum = 0
        for element in nums:
            total_sum += element
        
        left_sum = 0
        rigt_sum = 0
        n = len(nums)
        res = float('inf')
        res_idx = -1
        for idx in range(n):
            left_sum += nums[idx]
            right_sum = total_sum - left_sum
            n1 = idx+1
            n2 = n-n1
            left_avg = left_sum//n1
            right_avg = 0 if (idx == n-1) else right_sum//n2    
            diff = abs(left_avg - right_avg)
            if diff < res:
                res = diff
                res_idx = idx
        return res_idx