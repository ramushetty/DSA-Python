'''
Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.


Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
'''
from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d = {0: 1}
        prefix_sum, count = 0, 0
        for num in nums:
            prefix_sum = (prefix_sum + num) % k
            count += d.get(prefix_sum, 0)
            d[prefix_sum] = d.get(prefix_sum, 0) + 1
        return count

nums = [1,1,2,2,2,3]
k = 5
solution = Solution()
print(solution.subarraysDivByK(nums,k))