# Given two integer arrays nums1 and nums2, return an array of their intersection.
#  Each element in the result must be unique and you may return the result in any order.
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]

from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # return list(set(nums1) & set(nums2))

        res = []

        for i in nums1:

            if i not in res and i in nums2:
                res.append(i)
        return res

        # even we can do with hashmap




nums1 = [1,2,2,1]
nums2 = [2,2]
solution = Solution()
print(solution.intersection(nums1,nums2))