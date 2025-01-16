class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums_length = len(nums)
        nums.sort()
        for index in range(nums_length-3,-1,-1):
            if nums[index]+nums[index+1] > nums[index+2]:
                return nums[index] + nums[index+1] + nums[index+2]
        return 0