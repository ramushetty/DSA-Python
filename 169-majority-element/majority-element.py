class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele = None
        count = 0
        n = len(nums)
        for i in range(0,n):
            if count == 0:
                ele = nums[i]
                count = 1
            elif ele == nums[i]:
                count+=1
            else:
                count -=1
        count1 = 0
        for element in nums:
            if element == ele:
                count1+=1
        if count1 >= n//2:
            return ele

            
            
        