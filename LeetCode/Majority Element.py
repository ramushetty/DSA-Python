# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # s = set(nums)
        # m = len(nums)//2
        # for i in s:
        #     if nums.count(i) > m:
        #         return i

        # hashmap 

        count = 0
        candidate = None

        # Boyer-Moore Voting Algorithm
        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count +=  1
            else:
                count -=1
            # count += (1 if num == candidate else -1)

        return candidate    




nums = [2,2,1,1,1,2,2]
soluion = Solution()
print(soluion.majorityElement(nums))