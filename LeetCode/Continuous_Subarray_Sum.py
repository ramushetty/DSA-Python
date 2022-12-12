'''
Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
Note that:

A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
'''



from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        # for i in range(len(nums)):

        #     s = nums[i]
        #     for j in range(i+1, len(nums)):
        #         s += nums[j]
        #         if s % k == 0:
        #             return True
            
        # return False

        d = {0:-1}
        prefix_sum = 0
        for i,num in enumerate(nums):
            prefix_sum += num
            if k != 0:
                prefix_sum = prefix_sum % k
            if prefix_sum in d:
                if i - d[prefix_sum] > 1:
                    return True
            else:
                d[prefix_sum] = i
        return False




nums = [23,2,6,4,7]
k = 6
solution = Solution()
print(solution.checkSubarraySum(nums,k))