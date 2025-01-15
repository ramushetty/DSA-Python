class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = 0 # denotes 0
        j = 0 # denotes 1
        k = len(nums)-1 # denotes 2
        while j <= k:
            if nums[j] == 1:
                j +=1
            elif nums[j] == 2:
                temp = nums[j]
                nums[j] = nums[k]
                nums[k] = temp
                k -=1
            else:
                # i == 0
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i += 1
                j +=1
        