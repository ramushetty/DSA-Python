class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i,j = 0,0
        k = n-1

        while j<= k:
            if nums[j] == 1:
                j+=1
            elif nums[j] == 2:
                temp = nums[j]
                nums[j] = nums[k]
                nums[k] = temp
                k-=1
            else:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i+=1
                j+=1 


        