# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target is None:
            return -1
        if len(nums) == 1 and target == nums[0]:
            return 0
        if len(nums) == 1 and target != nums[0]:
            return -1
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = (start+end)//2
            if target == nums[mid]:
                return mid
            elif  nums[mid] > target:
                end = mid-1
            else:
                start = mid+1
        return -1



nums = [5]
target = 5
soultion = Solution()
print(soultion.search(nums,target))

