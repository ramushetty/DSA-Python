class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        element_dir = {}
        for i in range(n):
            temp = target - nums[i]
            if temp in element_dir:
                return [i,element_dir[temp]]
            else:
                element_dir[nums[i]] = i
        
        