# Input: nums = [6,5,4,8]
# Output: [2,1,0,3]

# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. 
# That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
from typing import List
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l = []
        n = sorted(nums)
        print(n)
        d = {}
        for i in range(len(n)):
            if n[i] not in d:
                d[n[i]] = i
        for i in nums:
            l.append(d[i])
        return l


nums = [6,5,1,6]
soluion = Solution()
print(soluion.smallerNumbersThanCurrent(nums))