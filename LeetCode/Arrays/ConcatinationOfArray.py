# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]

from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        temp_array = nums.copy()
        nums.extend(temp_array)
        return nums

nums = [1,2,1]
solution = Solution()
print(solution.getConcatenation(nums))