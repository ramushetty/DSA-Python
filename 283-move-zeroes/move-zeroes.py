class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        j = 0
        k=n-1
        if n==1:
            return
        while j<=k:
            if nums[j] == 0:
                j+=1
            else:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i+=1
                j+=1
        
                
        