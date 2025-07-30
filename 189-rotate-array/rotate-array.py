class Solution:
    def reverse(self,nums,start,end):
        while start < end:
            temp = nums[end]
            nums[end] = nums[start]
            nums[start] = temp
            start+=1
            end-=1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 1:
            return 
        k = k%n
        self.reverse(nums,0,n-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,n-1)


        