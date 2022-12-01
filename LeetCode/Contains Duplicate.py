# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

# Input: nums = [1,2,3,1]
# Output: true

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # s = set(nums)
        # if len(s) != len(nums):
        #     return True
        # return False

        # d = dict()
        # for i in nums:
        #     if i in d:
        #         d[i] += 1
        #     else:
        #         d[i] = 1
        # print(d)
        # for i in d.keys():
        #     if d[i] > 1:
        #         return True
        # return False 
        # 

        s = set()

        for i in nums:
            if i in s:
                return True
            else:
                s.add(i)
        return False       

nums = [1,2,3,4]
soluion = Solution()
print(soluion.containsDuplicate(nums))