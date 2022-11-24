# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# SC - O(n)
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start_index = 0
        for index in range(len(nums)):
            if nums[index] != val:
                nums[start_index] = nums[index]
                start_index += 1
        return start_index

        #another approach
        # start = 0
        # end = len(nums)
        # while start < end:
        #     if nums[start] == val:
        #         nums[start] = nums[end-1]
        #         end -= 1
        #     else:
        #         start += 1
        # return end
        



nums = [0,1,2,2,3,0,4,2]
val = 2
solution = Solution()
print(solution.removeElement(nums,val))