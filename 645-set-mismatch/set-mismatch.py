class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate , missing = -1, -1

        for index in range(len(nums)):
            if nums[abs(nums[index])-1] < 0:
                duplicate = abs(nums[index])
            else:
                nums[abs(nums[index])-1]  *=-1
        for index in range(len(nums)):
            if nums[index] > 0:
                missing = index+1
        return [duplicate,missing]
        