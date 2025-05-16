class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subarray_count = 0
        n = len(nums)
        sum_ = 0
        presummap = {0:1}
        for i in range(n):
            sum_ += nums[i]
            temp = sum_ - k
            if temp in presummap:
                subarray_count += presummap[temp]
            
            presummap[sum_] = 1+presummap.get(sum_,0)
        return subarray_count

        