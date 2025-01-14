class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # dir to store element and index position 
        element_index_dir = {}
        for i in range(0,len(nums)):
            temp = target - nums[i]
            if temp in element_index_dir:
                return [element_index_dir[temp],i]
            element_index_dir[nums[i]] = i
        # if no valid pair is found, return an empty list
        return []