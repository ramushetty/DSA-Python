# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

# Input: nums = [3,2,3]
# Output: [3]
# Input: nums = [1]
# Output: [1]
# Input: nums = [1,2]
# Output: [1,2]
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        t = len(nums) / 3
        print(t)
        print(d)
        l = []
        for i in d:
            if d[i] > t:
                l.append(i)
        return l


nums = [1,2]
soluion = Solution()
print(soluion.majorityElement(nums))