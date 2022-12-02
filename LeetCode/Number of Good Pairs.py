# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j]:
        #             count += 1
        # return count
        
        count = 0 
        hashmap = {}
        for n in nums:
            if n in hashmap:
                count += hashmap[n]
                hashmap[n] += 1
            else:
                hashmap[n] = 1
        return count
        

nums = [1,1,1,1]
soluion = Solution()
print(soluion.numIdenticalPairs(nums))