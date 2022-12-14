"""
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
"""


from typing import List
from collections import defaultdict

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        d = defaultdict(lambda: 0)
        max = 0
        for i in nums:
            if d[i] > 0:
                d[i] -= 1
                max += 1
                continue
            d[k-i] += 1


        return max
                


        




nums = [3,1,3,4,3]
k = 6   
solution = Solution()
print(solution.maxOperations(nums,k))