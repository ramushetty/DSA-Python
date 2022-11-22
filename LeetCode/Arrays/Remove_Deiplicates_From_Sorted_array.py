# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
#O(1)- SC
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insert_index = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[insert_index] = nums[i]
                insert_index += 1
        print(nums)
        return insert_index


nums = [1,1,2]
solution = Solution()
print(solution.removeDuplicates(nums))